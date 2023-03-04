#!/usr/bin/env python3
"""Class for manual object."""
import os
import requests
import bs4
from time import sleep
from utils.helper import first_word


class Manual:
    """Create a manual object."""

    def __init__(self, manual):
        """Create a object with chapters and attachments."""
        self.titulo = manual[0]
        self.link = manual[1]
        self.index = []
        self.dictionary = {}

    def list_chapters(self):
        """List a index with chapters."""
        print("Obtendo a lista de capítulos e anexos...")
        index = {}
        try:
            res = requests.get(self.link)
            res.raise_for_status()
            manual = bs4.BeautifulSoup(res.text, features="lxml")
            chapters = manual.select('a.internal-link')
            for item in chapters:
                index[item.getText()] = item.get('href')
            return index
        except Exception as exc:
            print(exc)
            sleep(3)
            print("Erro ao carregar a lista de capítulos.")

    def create_index(self):
        """Create a index of manual."""
        ind = self.list_chapters()
        self.dictionary = ind
        print("\nLista de Capítulos Atualizada.")
        lista = []
        num = 1
        for key, value in ind.items():
            print(f'[ {str.center(str(num), 4)} ] - {key} ')
            num += 1
            lista.append(key)
        self.index = lista

    def download_manual(self):
        """Download the entire manual."""
        pass

    def download_chapter(self, chapter):
        """Download DOC from URL to local directory.

        :param url: The url of the DOC file to be downloaded
        :return: True if DOC file was successfully downloaded, otherwise False.
        """
        # Request URL and get response object
        link = self.index[chapter-1]
        url = self.dictionary[link]
        response = requests.get(url, stream=True)
        folder = self.create_folder()
        # isolate DOC filename from URL
        doc_file_name = os.path.basename(url)
        if response.status_code == 200:
            # Save in new directory created by create_folder function
            filepath = os.path.join(folder, doc_file_name)
            with open(filepath, 'wb') as doc_object:
                doc_object.write(response.content)
                print(f'{doc_file_name} foi baixado com sucesso!')
                return True
        else:
            print(f'Ops! Não conseguimos baixar {doc_file_name}')
            print(f"Resposta do servidor: {response.status_code}")
            return False

    def create_folder(self):
        """Create a folder to save the manual."""
        title = first_word(self.titulo)  # Create a folder with first word
        path = os.path.join(os.getcwd(), title)
        if not os.path.isdir(path):
            os.mkdir(title)
        return path
