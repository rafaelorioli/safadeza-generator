#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    # Trata o arquivo palavras.txt para remover os verbos (palavras terminadas em ar,er,ir)
    with open('palavras.txt') as arquivo:
        palavra = arquivo.readline()
        palavra = palavra.lower()
        palavra = palavra.rstrip()

        while palavra:
            if palavra.endswith('ar'):
                palavra = arquivo.readline()
                palavra = palavra.lower()
                palavra = palavra.rstrip()
                continue

            if palavra.endswith('er'):
                palavra = arquivo.readline()
                palavra = palavra.lower()
                palavra = palavra.rstrip()
                continue

            if palavra.endswith('ir'):
                palavra = arquivo.readline()
                palavra = palavra.lower()
                palavra = palavra.rstrip()
                continue

            print(palavra)

            palavra = arquivo.readline()
            palavra = palavra.lower()
            palavra = palavra.rstrip()


if __name__ == "__main__":
    main()
