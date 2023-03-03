#!/usr/bin/env python3
"""Class for manual object."""

import requests
import bs4
from time import sleep

class Manual:
    """Create a manual object."""

    def __init__(self, manual):
        """Create a object with chapters and attachments."""
        self.titulo = manual[0]
        self.link = manual[1]

    def list_chapters(self):
        """List a index with chapters."""
        print("Obtendo a lista de capítulos...")
        index = {}
        try:
            res = requests.get(self.link)
            res.raise_for_status()
            manual = bs4.BeautifulSoup(res.text)
            chapters = manual.select('a.internal-link')
            for item in chapters:
                index[item.getText()] = item.get('href')
            return index
        except Exception as exc:
            print(exc)
            sleep(3)
            print("Erro ao carregar a lista de capítulos.")

    def download_manual(self):
        """Download the entire manual."""
        pass

    def download_chapter(self, chapter):
        """Download the specific chapter."""
        pass
