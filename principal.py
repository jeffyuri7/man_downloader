#!/usr/bin/env python3
"""Main module - It instancies objects to make the interface and logic."""

import list_manual
import download_manual
from time import sleep
from lib.interface.user_interface import UI
from utils.helper import clear


def main_principal(opc):
    """Create the logic of main menu."""
    clear()
    if opc == 1:
        list_manual.main()
    if opc == 2:
        download_manual.main()


while True:
    try:
        clear()
        ui = UI("MANUAL DOWNLOADER")
        ui.header()
        options = ["Listar Manuais disponíveis", "Baixar Manual", "Sair"]
        option = ui.menu(options)
        if 0 < option < 3:
            main_principal(option)
            continue
        elif option == 3:
            ui.exitTo()
            break
        elif option is None:
            raise TypeError
        else:
            print("ERRO! Opção inválida! Digite um número de opção válido.")
            sleep(2)
            continue
    except TypeError:
        print("Erro, opção inválida! Digite apenas o número da opção.")
        sleep(2)
        continue
