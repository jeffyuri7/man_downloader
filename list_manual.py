#!/usr/bin/env python3
"""This module lists all available manuals to download."""

import requests
import bs4
from time import sleep
from lib.interface.user_interface import UI
from utils.helper import clear


def list_manuals():
    """List all available manuals."""
    print("Obtendo a lista de manuais...")
    library = update_manuals()
    return library


def update_manuals(link='https://intranet.correios.com.br/ect-normas'):
    """Update the DB of manuals."""
    library = {}
    while True:
        try:
            res = requests.get(link)
            res.raise_for_status()
            # TODO fuction to update link. If a new link inserted,
            # the link will be updated in database
            # bd.update_link(link)
            correios_normas = bs4.BeautifulSoup(res.text, features="lxml")
            links = correios_normas.select('.titulo-marcadores-1 > a[href]')
            for item in links:
                library[item.getText()] = item.get('href')
            return library
        except Exception as exc:
            print(exc)
            sleep(10)
            response = input("Houve um problema com o servidor ao tentar atualizar a lista de Manuais.\n\nDeseja tentar novamente? [ S/N ]")
            if response in 'Ss':
                print(f'Link atual na base de dados: {link}')
                print("Deseja passar um novo link para atualizar a base de dados?")
                print("Utilize essa opção apenas se o link acima for alterado.")
                while True:
                    option = input("Sua resposta: [ S/N ]")
                    if option in 'Ss':
                        link = input("Digite o novo link: ")
                        print("Atualizando link e base de dados...")
                        sleep(2)
                        break
                    elif option in 'Nn':
                        print('Ok, vamos tentar novamente com o link padrão.')
                        sleep(2)
                        break
                    else:
                        print("Opção inválida! Tente novamente.")
            elif response in 'Nn':
                print("Ok, cancelando operação.")
                break


def main():
    """Execute the main function."""
    while True:
        try:
            clear()
            ui_list = UI("LISTA DE MANUAIS DISPONÍVEIS")
            ui_list.header()
            list_man = list_manuals()
            option = ui_list.menu_manuals(list_man)
            clear()
            ui_list = UI("LISTA DE MANUAIS DISPONÍVEIS")
            ui_list.header()
            print(f"Selecionado {option}")
            sleep(1)
            # TODO implements the download of manual.
            confirm = input(f'\nDeseja baixar o {option}? [ S/N ]')
            if confirm in 'Ss':
                print("Baixando manual...")
                return list_man[option]
                sleep(5)
            elif confirm in 'Nn':
                clear()
                print("Ok, selecione o manual correto")
                continue
            else:
                print("Opção inválida! Tente novamente.")
        except Exception:
            print("ERRO! Opção inválida! Digite apenas o número da opção.")
            sleep(2)
            continue


if __name__ == '__main__':
    main()
