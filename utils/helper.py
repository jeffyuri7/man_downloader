#!/usr/bin/env python3
"""Contains some helpers to man_downloader."""

import os


def clear():
    """Clear the terminal."""
    os.system('clear')

def first_word(string):
    """Capture the first word of a string."""
    inicio = fim = None
    for i, c in enumerate(string):
        letra = c.isalpha()
        if inicio is None and letra:
            inicio = i # início de palavra
        elif inicio is not None and fim is None and not letra:
            fim = i # fim de palavra
            break # sai do loop
    else: # chegou ao fim da string e não encontrou um caractere que não é letra
        fim = len(string)

    if inicio is not None and fim is not None:
        primeira_palavra = string[inicio:fim]
        print(primeira_palavra)
    else:
        print('A frase não contém nenhuma palavra')
