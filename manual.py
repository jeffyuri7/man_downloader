#!/usr/bin/env python3
"""Class for manual object."""
import os
import requests
import bs4
from time import sleep
from utils.helper import first_word
from utils.database import DB
from document import Document


class Manual:
    """Create a manual object."""

    def __init__(self, id_manual, titulo, link):
        """Create a object with chapters and attachments."""
        self.id_manual = id_manual  # ID of manual in database
        self.titulo = titulo  # Title of manual in database
        self.link = link  # Link of manual in database
        self.index = []

    def update_manual_chapters(self, db):
        """List a index with chapters."""
        print("Baixando a lista de capítulos e anexos...")
        try:
            res = requests.get(self.link)
            res.raise_for_status()
            manual = bs4.BeautifulSoup(res.text, features="lxml")
            chapters = manual.select('a.internal-link')
            index = [(self.id_manual, (item.getText()).strip(), (item.get('href')).strip(), order) for order, item in enumerate(chapters, 1)]
            db.update_manual(index)
        except Exception as exc:
            print(exc)
            sleep(3)
            print("Erro ao carregar a lista de capítulos.")

    def list_chapters(self, db):
        """Consult DB and generate a index of manual."""
        try:
            self.index = db.list_manual(self.id_manual)
        except Exception as exc:
            print(exc)
            sleep(3)
            print("Erro ao carregar a lista de capítulos.")

    def show_content_manual(self, db):
        """Show the content of index manual."""
        print("Recuperando a lista de capítulos e anexos...")
        self.list_chapters(db)
        print(*((f'[ {str.rjust(str(item[4]), 2)} ] - {item[1]}') for item in self.index), sep='\n')

    def download_manual(self, db):
        """Download the entire manual."""
        print(f"ATENÇÃO: Agora será realizado o download do {self.titulo} completo.")
        print("\nEssa operação pode demorar muito tempo, dependendo do tamanho da quantidade de arquivos e da velocidade da sua conexão.")
        folder = self.create_folder()
        print(f"Os arquivos serão salvos na seguinte pasta: {folder}")
        if not self.index:
            self.list_chapters(db)
        for item in self.index:
            print(f"\n - Baixando {item[1]}")
            chapter = Document(item[0], item[1], item[2], item[3])
            chapter.download_document(folder)
            print(f" - {item[1]} baixado com sucesso!\n")
        print("\nDownload concluído.")
        print(f'O {self.titulo} foi baixado com sucesso!')

    def create_folder(self):
        """Create a folder to save the manual."""
        title = first_word(self.titulo)  # Create a folder with first word
        path = os.path.join(os.getcwd(), title)
        if not os.path.isdir(path):
            os.mkdir(title)
        return path

if __name__ == '__main__':
    db = DB()
    man = Manual(2, "MANCOD - Manual de Conduta Disciplinar", "https://intranet.correios.com.br/ect-normas/mancod")
    # man.show_content_manual(db)
    # man.download_manual(db)

    lista = db.list_library()
    print(lista)
