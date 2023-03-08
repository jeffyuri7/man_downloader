#!/usr/bin/env python3
"""Class module to create a library of manuals."""

import requests
import bs4
from time import sleep
from utils.database import DB
from manual import Manual


class Library:
    """Create a library of manuals."""

    def __init__(self):
        """Construct the library object."""
        self.all_manuals = []  # A list with all manuals
        self.link = ''

    def list_manuals(self, db):
        """List all manuals of library."""
        self.all_manuals = db.list_library()

    def show_list_manuals(self, db):
        """Show a list of manuals retrieved of local database."""
        print("=" * 70)
        print(str.center("Recuperando a lista de manuais...", 70))
        print("=" * 70)
        print()
        if not self.all_manuals:
            self.list_manuals(db)
        print(*((f'[ {str.rjust(str(ordem), 2)} ] - {item[1]}') for ordem, item in enumerate(self.all_manuals, 1)), sep='\n')

    def download_all_manuals(self):
        """Download all manuals of library."""
        pass

    def sync_library(self, db):
        """Sync data with server before update the local database."""
        print("=" * 70)
        print(str.center("Sincronizando a lista de manuais com o servidor...", 70))
        print("=" * 70)
        print()
        try:
            # First, check if self.all_manuals alredy exists. If it doesn't
            # exist we call list_manuals function that set this var.
            if not self.all_manuals:
                self.list_manuals(db)

            # Retrieve link of local database.
            self.link = db.consult_link()

            # Start request to server.
            res = requests.get(self.link)
            res.raise_for_status()
            manuals_bs4 = bs4.BeautifulSoup(res.text, features="lxml")
            manuals = manuals_bs4.select('.titulo-marcadores-1 > a[href]')

            # Create a iter with download data.
            index_library = [((item.getText()).strip(), (item.get('href')).strip()) for item in manuals]
            if not index_library:
                raise Exception()
            return index_library
        except Exception as exc:
            print(exc)
            sleep(1)
            print("=" * 70)
            print(str.center("Erro ao carregar os dados do servidor.", 70))
            print("=" * 70)
            print()

    def update_manuals(self, db):
        """Add one manual to library."""
        try:
            index_library = self.sync_library(db)
            if not index_library:
                raise Exception()
            # Create a iter with data to compare with download data.
            list_currently = [(item[1], item[2]) for item in self.all_manuals]
            # Compare the two iter. In first comparison the difference
            # will be add to database. In second comparison the difference
            # will be delete of database. This will become the local database
            # and server equals.
            # Call function that realize the update in local database.
            data_add = list(set(index_library).difference(list_currently))
            db.update_library(data_add)

            # Now, we consult again the db to examine if there is
            # one manual that don't exists in server.
            # If there is one remove_manual_from_library removes it.
            self.list_manuals(db)
            list_currently = [(item[1], item[2]) for item in self.all_manuals]
            data_rem = [(item[0],) for item in (list(set(list_currently).difference(index_library)))]
            if data_rem:
                db.remove_manual_from_library(data_rem)
            print("Banco de dados atualizado com sucesso.")
        except Exception as exc:
            print(exc)
            sleep(1)
            print("=" * 70)
            print(str.center("Erro ao carregar a lista de capítulos.", 70))
            print("=" * 70)
            print()

    def update_library(self, db):
        """Update manuals and documents."""
        try:
            update_lib = self.update_manuals(db)
            if not update_lib:
                raise Exception()
            for item in self.all_manuals:
                manual = Manual(item)
                manual.update_manual_chapters(db)
        except Exception as exc:
            print(exc)
            sleep(1)
            print("=" * 70)
            print(str.center("Verifique a sua conexão com a INTRANET. Lembre-se", 70))
            print(str.center("de estar conectado a intranet para atualizar o banco de dados.", 70))
            print("=" * 70)




if __name__ == '__main__':
    db = DB()
    library = Library()
    # library.update_library(db)
    # library.list_manuals(db)
    library.show_list_manuals(db)
