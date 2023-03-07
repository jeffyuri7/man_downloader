#!/usr/bin/env python3
"""Class module to create a library of manuals."""

import requests
import bs4
from time import sleep
from utils.database import DB


class Library:
    """Create a library of manuals."""

    def __init__(self):
        """Construct the library object."""
        self.all_manuals = []  # A list with all manuals
        self.link = ''

    def list_manuals(self, db):
        """List all manuals of library."""
        print("Recuperando a lista de manuais...")
        self.all_manuals = db.list_library()
        sleep(1)
        print(*((f'[ {str.rjust(str(ordem), 2)} ] - {item[1]}') for ordem, item in enumerate(self.all_manuals, 1)), sep='\n')

    def download_all_manuals(self):
        """Download all manuals of library."""
        pass

    def update_manuals(self, db):
        """Add one manual to library."""
        print("Sincronizando a lista de manuais com o servidor...")
        try:
            # First, check if self.all_manuals alredy exists. If it doesn't
            # exist we call list_manuals function that set this var.
            if not self.all_manuals:
                self.list_manuals(db)

            # Create a iter with data to compare with download data.
            list_currently = [(item[1], item[2]) for item in self.all_manuals]

            # Retrieve link of local database.
            self.link = db.consult_link()

            # Start request to server.
            res = requests.get(self.link)
            res.raise_for_status()
            manuals_bs4 = bs4.BeautifulSoup(res.text, features="lxml")
            manuals = manuals_bs4.select('.titulo-marcadores-1 > a[href]')

            # Create a iter with download data.
            index_library = [((item.getText()).strip(), (item.get('href')).strip()) for item in manuals]

            # Compare the two iter. In first comparison the difference
            # will be add to database. In second comparison the difference
            # will be delete of database. This will become the local database
            # and server equals.
            data_add = list(set(index_library).difference(list_currently))
            data_rem = [(item[0],) for item in (list(set(list_currently).difference(index_library)))]

            # Call function that realize the update in local database.
            db.update_library(data_add, data_rem)
        except Exception as exc:
            print(exc)
            sleep(3)
            print("Erro ao carregar a lista de capítulos.")


    def remove_manual(self):
        """Remove one manual of library."""
        pass

if __name__ == '__main__':
    db = DB()
    library = Library()
    library.update_manuals(db)
    # library.list_manuals(db)
