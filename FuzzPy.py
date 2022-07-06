#!/usr/bin/env python
# -*- utf-8 -*-

import argparse
import requests
from multiprocessing import Pool as tp
import time
import urllib3
from banners import rBanner as rb
from tqdm import tqdm


class Fuzzer:
    # TODO Método inicial da classe
    def __init__(self, args):
        global lista
        self.args = args
        self.tempo_inicial = time.time()
        self.OK = '\033[92m'  # GREEN
        self.RESET = '\033[0m'  # RESET COLOR
        self.WARNING = '\033[93m'  # YELLOW
        self.s = requests.Session()
    # TODO Método que executa toda a lógica da classe

    def run(self):
        lista = self.wordlist()
        if args.banner == 's':
            self.banner(lista)
        if self.args.target and self.args.extensions:
            self.fuzz_extension_on_target(lista)
        elif self.args.target:
            self.fuzz_target(lista)

    # TODO Método que trata e imprime o banner
    def banner(self, list):
        banner = rb.random_banner()
        print(banner)
        time.sleep(2)
        print('-'*50)
        print('Autor: Lucas dSilva')
        print('-'*50)
        print(f'Target: {args.target}')
        print('-'*50)
        if self.args.extensions:
            print(f'Extensões: {args.extensions}')
        else:
            print('Extensões: None')
        print('-'*50)
        if args.simple == 's':
            print("Modo: simples")
        else:
            print("Modo: normal")
        print('-'*50)
        if self.args.wordlist:
            print(f"Wordlist: {args.wordlist}")
        else:
            print("Wordlist: padrão")
        print('-'*50)
        wc = len(list)
        print(f"Número de linhas: {wc}")
        print("-"*50)
        print(f"Threads: {args.threads}")
        print("-"*50)

    # TODO Método que vrifica se o parâmetro (-o) está ativo e usa o caminho para criar o arquivo de saída e as salva nele
    def save_in_output(self, found):
        if self.args.output:
            with open(args.output, 'w+') as file:
                if found == None:
                    pass
                else:
                    file.write(found)
                    file.write('\n')

    
    # TODO Método que monta e realiza as requisições sem as extensões ao alvo

    def work(self, word):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        url_final = f'{args.target}{word}'
        if args.simple == 's':
            try:
                r = self.s.get(url_final, stream=True,
                               verify=False, timeout=10)
                if r.status_code < 400:
                    return f"{self.OK}{url_final}{self.RESET}"
            except:
                pass

        else:
            try:
                r = self.s.get(url_final, stream=True,
                               verify=False, timeout=10)
                if r.status_code < 400:
                    return f"{self.OK}Found[*]:{self.RESET} {url_final}{self.RESET}"
            except:
                pass
    # TODO Método que monta e realiza as requisições com as extensões ao alvo

    def work_ext(self, word):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        extensoes = args.extensions
        extensoes = extensoes.split(',')
        if args.simple == 's':
            for ext in extensoes:
                if '.' not in ext:
                    ext = '.'+ext
                    url_final = f'{args.target}{word}{ext}'
                    try:
                        r = self.s.get(url_final, stream=True,
                                       verify=False, timeout=10)
                        if r.status_code < 400:
                            return f"{self.OK}{url_final}{self.RESET}"
                        continue
                    except:
                        pass
                else:
                    url_final = f'{args.target}{word}{ext}'
                    try:
                        r = self.s.get(url_final, stream=True,
                                       verify=False, timeout=10)
                        if r.status_code < 400:
                            return f"{self.OK}{url_final}{self.RESET}"
                        continue
                    except:
                        pass
        else:
            for ext in extensoes:
                if '.' not in ext:
                    ext = '.'+ext
                    url_final = f'{args.target}{word}{ext}'
                    try:
                        r = self.s.get(url_final, stream=True,
                                       verify=False, timeout=10)
                        if r.status_code <400:
                            return f"{self.OK}Found[*]:{self.RESET} {url_final}{self.RESET}"
                        continue
                    except:
                        pass
                else:
                    url_final = f'{args.target}{word}{ext}'
                    try:
                        r = self.s.get(url_final, stream=True,
                                       verify=False, timeout=10)
                        if r.status_code < 400:
                            return f"{self.OK}Found[*]:{self.RESET} {url_final}{self.RESET}"
                        continue
                    except:
                        pass

    # TODO Método que faz o fuzzing sem extensões

    def fuzz_target(self, wordlist):
        try:
            with tp(processes=args.threads) as p:
                max_ = len(wordlist)
                with tqdm(total=max_,ascii=True,colour="green") as pbar:
                    for r in p.imap_unordered(self.work, wordlist):
                        if r != None:
                            tqdm.write("")
                            tqdm.write(f"{r}")
                            self.save_in_output(r)
                        pbar.update()
        except KeyboardInterrupt:
            print("\nParando a execução")
        finally:
            tempo_final = time.time()
            tempo_exec = tempo_final-self.tempo_inicial
            if tempo_exec >= 60:
                tempo_exec = tempo_exec/60
                print("O processo levou: %.2f minutos para ser executado" %
                      (tempo_exec))
            else:
                print("O processo levou: %.2f segundos para ser executado" %
                      (tempo_exec))

    # TODO Método que faz o fuzzing com extensões

    def fuzz_extension_on_target(self, wordlist):
        try:
            with tp(processes=args.threads) as p:
                max_ = len(wordlist)
                with tqdm(total=max_,ascii=True,colour='green') as pbar:
                    for r in p.imap_unordered(self.work_ext, wordlist):
                        if r != None:
                            tqdm.write("")
                            tqdm.write(f"{r}")
                            self.save_in_output(r)
                        pbar.update()
            with tp(processes=args.threads) as p:
                max_ = len(wordlist)
                with tqdm(total=max_,ascii=True,colour='green') as pbar:
                    for r in p.imap_unordered(self.work, wordlist):
                        if r != None:
                            tqdm.write("")
                            tqdm.write(f"{r}")
                            self.save_in_output(r)
                        pbar.update()
        except KeyboardInterrupt:
            print("\nParando a execução")
        finally:
            tempo_final = time.time()
            tempo_exec = tempo_final-self.tempo_inicial
            if tempo_exec >= 60:
                tempo_exec = tempo_exec/60
                print("O processo levou: %.2f minutos para ser executado" %
                      (tempo_exec))
            else:
                print("O processo levou: %.2f segundos para ser executado" %
                      (tempo_exec))

    # TODO Método que define e trata a wordlist
    def wordlist(self):
        if self.args.wordlist:
            with open(args.wordlist, 'r') as file:
                lista = file.read()
            lista = lista.split('\n')
        else:
            with open('res/standart-wordlist.txt', 'r')as file:  # res/standart-wordlist.txt
                lista = file.read()
                lista = lista.strip()
            lista = lista.split('\n')
        return lista


# TODO tratamento dos argumentos
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="FuzzPY\n by:Lucas dSilva")
    parser.add_argument('-t', '--target', type=str, help='A url do alvo')
    parser.add_argument('-w', '--wordlist', type=str,
                        help='O caminho da wordlist escolhida')
    parser.add_argument('-e', '--extensions', type=str,
                        help='As extensões que desja testar')
    parser.add_argument('-s', '--simple', default='n',
                        type=str, help='Ativa ou desativa o simple mode s=para ativar\n n=desativa(Padrão)')
    parser.add_argument('-b', '--banner', default='s', type=str,
                        help="Ativa o desativa o cabeçalho do programa:\n s=Para ativar(Padrão)\nn=para desativar")
    parser.add_argument('-o', '--output', type=str,
                        help='Ative para guardar a saida do programa em um arquivo')
    parser.add_argument('-th', '--threads', type=int, default=40,
                        help='Coloque o número de threads que deseja')

    args = parser.parse_args()

    fp = Fuzzer(args)
    fp.run()
