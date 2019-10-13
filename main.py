#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import tweepy
import sys
import os

consumer_key = os.environ['consumer_key']
consumer_secret =  os.environ['consumer_secret']

access_token =  os.environ['access_token']
access_token_secret =  os.environ['access_token_secret']

print(consumer_key)
print(consumer_secret)
print(access_token)
print(access_token_secret)

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None


def main():
    verbo_escolhido = escolher_verbo()
    print('Verbo escolhido --> ' + verbo_escolhido)

    palavra_escolhida = escolher_palavra()
    print('Palavra escolhida --> ' + palavra_escolhida + '\n')

    frase = gerar_frase(palavra_escolhida, verbo_escolhido)
    print('Frase  --> ' + frase + '\n')

    oauth = OAuth()
    api = tweepy.API(oauth)

    if (len(sys.argv) > 1 and sys.argv[1] == '--post-to-twitter'):

        try:
            api.update_status(frase)
        except Exception as e:
            print('Não foi possível postar no Twitter, verifique o processo de autenticação.')
            exit(1)

        print('\nEnviado ao twitter o post.')
    else:
        print('Não foi utilizado a flag --post-to-twitter para enviar a frase para o Twitter.')


def gerar_frase(palavra_escolhida, verbo_escolhido):
    if palavra_escolhida.endswith('a'):
        frase = verbo_escolhido + ' a ' + palavra_escolhida
    else:
        frase = verbo_escolhido + ' o ' + palavra_escolhida
    return frase


def escolher_palavra():
    with open('palavras_sem_verbos.txt') as palavras_sem_verbos:
        lista_palavras_sem_verbos = palavras_sem_verbos.read().split('\n')
        palavra_escolhida = random.choice(lista_palavras_sem_verbos)
    return palavra_escolhida


def escolher_verbo():
    with open('verbos.txt') as verbos:
        lista_verbos = verbos.read().split('\n')
        verbo_escolhido = random.choice(lista_verbos)
    return verbo_escolhido


if __name__ == "__main__":
    main()
