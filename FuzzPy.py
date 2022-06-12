#!/bin/bash
# -*- utf-8 -*-

import argparse
import requests
from joblib import Parallel, delayed
import time
from banners import rBanner as rb

class Fuzzer:
    # TODO Método inicial da classe
    def __init__(self, args):
        self.args = args
        self.tempo_inicial = time.time()
        self.OK = '\033[92m'  # GREEN
        self.RESET = '\033[0m'  # RESET COLOR
        self.WARNING = '\033[93m'  # YELLOW
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
        print(self.OK+banner+self.RESET)
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

    # TODO Método que monta e realiza as requisições sem as extensões ao alvo

    def work(self, word):
        url_final = f'{args.target}{word}'
        if args.simple == 's':
            try:
                r = requests.get(url_final, stream=True,
                                 verify=False, timeout=10)
                if r.status_code <= 403:
                    print(f"{url_final}")
            except:
                pass

        else:
            try:
                r = requests.get(url_final, stream=True,
                                 verify=False, timeout=10)
                if r.status_code <= 403:
                    if r.status_code == 200:
                        print(
                            f"{self.OK}Found:{self.RESET} {url_final} CODE:{self.OK}<{r.status_code}>{self.RESET}")
                    else:
                        print(
                            f"{self.OK}Found:{self.RESET} {url_final} CODE:{self.WARNING}<{r.status_code}>{self.RESET}")
            except:
                pass

    # TODO Método que monta e realiza as requisições com as extensões ao alvo

    def work_ext(self, word):
        extensoes = args.extensions
        extensoes = extensoes.split(',')
        if args.simple == 's':
            for ext in extensoes:
                if '.' not in ext:
                    extp = '.'+ext
                url_final = f'{args.target}{word}{ext}'
                try:
                    r = requests.get(url_final, stream=True,
                                     verify=False, timeout=10)
                    if r.status_code <= 403:
                        print(f"{url_final}")
                except:
                    pass
        else:
            for ext in extensoes:
                if '.' not in ext:
                    ext = '.'+ext
                url_final = f'{args.target}{word}{ext}'
                try:
                    r = requests.get(url_final, stream=True,
                                     verify=False, timeout=10)
                    if r.status_code <= 403:
                        if r.status_code == 200:
                            print(
                                f"{self.OK}Found:{self.RESET} {url_final} CODE:{self.OK}<{r.status_code}>{self.RESET}")
                        else:
                            print(
                                f"{self.OK}Found:{self.RESET} {url_final} CODE:{self.WARNING}<{r.status_code}>{self.RESET}")
                except:
                    pass

    # TODO Método que faz o fuzzing sem extensões

    def fuzz_target(self, wordlist):
        try:
            resultado = Parallel(n_jobs=35)(
                delayed(self.work)(word)for word in wordlist)
        except KeyboardInterrupt:
            print("\nParando a execução")
        else:
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
            resultado = Parallel(n_jobs=50)(
                delayed(self.work_ext)(word) for word in wordlist)
            resultado2 = Parallel(n_jobs=50)(
                delayed(self.work)(word)for word in wordlist)
        except KeyboardInterrupt:
            print("\nParando a execução")
        else:
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
    # target,extensions,wordlist,Talvez(output),banner,simplemode
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
    args = parser.parse_args()

    fp = Fuzzer(args)
    fp.run()
