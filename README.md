<h1 align="center">FUzzPy</h1>

<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
<img src="http://img.shields.io/static/v1?label=VERSION&message=1.4&color=blue&style=for-the-badge"/>
<img src="https://img.shields.io/github/license/accessmaker/FUzzPy?style=for-the-badge"/>
</p>



Um simples web fuzzer feito em python.

<h2>INSTALL:</h2>

git clone https://github.com/accessmaker/FUzzPy

pip install -r requiriments.txt

<h2>USAGE:</h2>

python3 FuzzPy.py -h

usage: FuzzPy.py [-h] [-t TARGET] [-w WORDLIST]
                 [-e EXTENSIONS] [-s SIMPLE]
                 [-b BANNER] [-o OUTPUT]
                 [-th THREADS]

FuzzPY by:Lucas dSilva

optional arguments:

  -h, --help            show this help message and
                        exit.
                        
  -t TARGET, --target TARGET
                        A url do alvo.
                        
  -w WORDLIST, --wordlist WORDLIST
                        O caminho da wordlist
                        escolhida.
                        
  -e EXTENSIONS, --extensions EXTENSIONS
                        As extensões que desja
                        testar.
                        
  -s SIMPLE, --simple SIMPLE
                        Ativa ou desativa o simple
                        mode s=para ativar
                        n=desativa(Padrão).
                        
  -b BANNER, --banner BANNER
                        Ativa o desativa o
                        cabeçalho do programa:
                        s=Para ativar(Padrão)
                        n=para desativar.
                        
  -o OUTPUT, --output OUTPUT
                        Ative para guardar a saida
                        do programa em um arquivo.
                        
  -th THREADS, --threads THREADS
                        Coloque o número d threads
                        que deseja.
                        
<h2>FUNCTIONALITY</h2>

'Funcionalidade': Ele usa a biblioteca requests para tentar listar os diretórios ou arquivos de uma aplicação web por meio de uma wordlist.
