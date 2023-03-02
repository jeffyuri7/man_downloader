#!/usr/bin/env python3
"""This module gets the selected manual and download it."""

import os
import requests
from time import sleep


def download_doc_file(url: str) -> bool:
    """Download DOC from URL to local directory.

    :param url: The url of the DOC file to be downloaded
    :return: True if DOC file was successfully downloaded, otherwise False.
    """
    # Request URL and get response object
    response = requests.get(url, stream=True)

    # isolate DOC filename from URL
    doc_file_name = os.path.basename(url)
    if response.status_code == 200:
        # Save in current working directory
        filepath = os.path.join(os.getcwd(), doc_file_name)
        with open(filepath, 'wb') as doc_object:
            doc_object.write(response.content)
            print(f'{doc_file_name} foi baixado com sucesso!')
            return True
    else:
        print(f'Uh oh! Não conseguimos baixar {doc_file_name}')
        print(f"Resposta do servidor: {response.status_code}")
        return False


def main():
    """Download the selected manual."""
    URL = 'https://intranet.correios.com.br/ect-normas/manafi/copy16_of_MANAFIMDULO01CAPTULO001_Anexo01.doc'
    download_doc_file(URL)
    sleep(2)


if __name__ == '__main__':
    URL = 'https://intranet.correios.com.br/ect-normas/manafi/copy16_of_MANAFIMDULO01CAPTULO001_Anexo01.doc'
    download_doc_file(URL)
    sleep(2)
