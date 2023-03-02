#!/usr/bin/env python3
"""Main module - It instancies objects to make the interface and logic."""

import os
from time import sleep
from lib.interface.user_interface import UI


clear = lambda: os.system('clear')


def main_principal(opc):
    """Create the logic of main menu."""
    clear()
    if opc == 1:
        pass


while True:
    try:
        clear()
        ui = UI("MANUAL DOWNLOADER")
        ui.header()
        options = ["Listar Manuais disponíveis", "Baixar Manual", "Sair"]
        option = ui.menu(options)
        if option == 1:
            continue
        else:
            break
    except:
        print("Erro, opção inválida! Tente novamente.")
        sleep(2)
        continue
