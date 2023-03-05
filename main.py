#!/usr/bin/env python3
"""Main module - It instancies objects to make the interface and logic."""

import list_manual
from manual import Manual
from time import sleep
from lib.interface.user_interface import UI
from utils.helper import clear
from utils.database import DB


def main_principal(opc):
    """Create the logic of main menu."""
    clear()
    while True:
        if opc == 1:
            choice = list_manual.list_manuals(db)
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
            if choice2 == 2:
                print("Atenção")
                print("Essa opção pode demorar um tempo considerável.")
                choice4 = input("\nDeseja baixar o manual completo? [ S/N ]")
                if choice4 in 'Ss':
                    manual.download_manual()
                    break
                else:
                    print("Ok, voltando para o menu anterior...")
                    break
            else:
                print("Opção inválida! Tente novamente.")
                continue
            sleep(3)
        if opc == 2:
            print("Deseja atualizar o banco de dados local?")
            print("Observação: Utilize essa opção para listar novos manuais ou novos arquivos dos manuais existentes.")
            choice5 = input("Confirma a atualização do banco de dados?")
            if choice5 in 'Ss':
                print("Atualizando a lista com o servidor...")
                list_manual.update_manuals()
                print("Lista de capítulos e anexos atualizado com sucesso.")
                print("\nDirecionando para a página de Downloads...")
                opc = 1
                continue
            if choice5 in 'Nn':
                print("Ok, iremos direcioná-lo para a página de Downloads.")
                opc = 1
                continue

while True:
    try:
        clear()
        ui = UI("MANUAL DOWNLOADER")
        ui.header()
        db = DB()
        db.list_library()
        options = ["Listar Manuais disponíveis","Atualizar Lista dos Manuais","Sair"]
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
    except KeyboardInterrupt:
        ui.exitTo()
