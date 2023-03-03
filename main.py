#!/usr/bin/env python3
"""Main module - It instancies objects to make the interface and logic."""

from manual import Manual
import list_manual
from time import sleep
from lib.interface.user_interface import UI
from utils.helper import clear


def main_principal(opc):
    """Create the logic of main menu."""
    clear()
    if opc == 1:
        while True:
            choice = list_manual.main()
            manual = Manual(choice)
            print("\nSelecione a opção desejada:")
            print("[ 1 ] - Ver a lista de capítulos")
            print("[ 2 ] - Baixar o Manual Completo")
            choice2 = ui.inputInt("Sua opção: ")
            if choice2 == 1:
                manual.create_index()
                print(ui.line())
                print("Digite o número do capítulo desejado para baixar, ou digite 0 para baixar o manual completo.")
                choice3 = ui.inputInt("Sua Opção: ")
                if choice3 == 0:
                    manual.download_manual()
                    break
                manual.download_chapter(choice3)
            elif choice2 == 3:
                manual.download_manual()
                break
            else:
                print("Opção inválida! Tente novamente.")
                continue
            sleep(3)


while True:
    try:
        clear()
        ui = UI("MANUAL DOWNLOADER")
        ui.header()
        options = ["Listar Manuais disponíveis","Sair"]
        option = ui.menu(options)
        if 0 < option < 2:
            main_principal(option)
            continue
        elif option == 2:
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
    except KeyboardInterrupt:
        ui.exitTo()
