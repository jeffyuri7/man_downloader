#!/usr/bin/env python3
"""This module include the logical about database."""

import sqlite3


class DB:
    """Create a database object."""

    def __init__(self):
        """Create a database object."""
        self.conn = sqlite3.connect('database.sqlite3')

    def update_library(self, data):
        """Update the entire library."""
        # list_manuals must be a list of tuples. Each tuple should have
        # title and link of a manual.
        try:
            self.cur = self.conn.cursor()
            self.cur.executemany("INSERT INTO manuals (titulo, link) VALUES (?, ?)", data)
            print("Banco de dados atualizado com sucesso.")
        except Exception as exc:
            print("Houve um erro ao atualizar o bando de dados.")
            print("Código do erro", exc)
            print("O banco de dados não foi atualizado.")
        finally:
            self.cur.close()
            self.conn.commit()

    def update(self):
        """Update the database."""
        pass

    def select(self):
        """Select data in database."""
        pass

    def update_link(self, link):
        """Update the link if it change."""
        pass
