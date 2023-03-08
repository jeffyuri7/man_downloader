#!/usr/bin/env python3
"""This module include the logical about database."""

import sqlite3


class DB:
    """Create a database object."""

    def __init__(self):
        """Create a database object."""
        self.conn = sqlite3.connect('database.sqlite3')

    def update_library(self, data_add):
        """Update the entire library."""
        # list_manuals must be a list of tuples. Each tuple should have
        # title and link of a manual.
        try:
            self.cur = self.conn.cursor()
            for item in data_add:
                self.cur.execute("INSERT INTO manuals (titulo, link) VALUES (?, ?) ON CONFLICT(titulo) DO UPDATE SET link=?", (item[0], item[1],item[1]))
                print("Novo manual inserido ou link atualizado.")
        except Exception as exc:
            print("Houve um erro ao inserir novos manuais no bando de dados.")
            print("Código do erro", exc)
            print("O banco de dados não foi atualizado.")
        finally:
            self.cur.close()
            self.conn.commit()

    def remove_manual_from_library(self, data_rem):
        """Remove one manual of local database."""
        try:
            self.cur = self.conn.cursor()
            self.cur.executemany("DELETE FROM manuals WHERE titulo = ?", data_rem)
            print("Manual antigo foi excluído.")
        except Exception as exc:
            print("Houve um excluir dados antigos do bando de dados.")
            print("Código do erro", exc)
            print("O banco de dados não foi atualizado.")
        finally:
            self.cur.close()
            self.conn.commit()



    def update_manual(self, data):
        """Update the chapters and attachments of a manual."""
        try:
            self.cur = self.conn.cursor()
            self.cur.executemany("INSERT OR IGNORE INTO documentos (manual_id, cap_anexo, link, ordem) VALUES (?, ?, ?, ?)", data)
            print("Banco de dados atualizado com sucesso.")
        except Exception as exc:
            print("Houve um erro ao atualizar o bando de dados.")
            print("Código do erro", exc)
            print("O banco de dados não foi atualizado.")
        finally:
            self.cur.close()
            self.conn.commit()

    def list_library(self):
        """List all manuals of library."""
        try:
            self.cur = self.conn.cursor()
            cursor = self.cur.execute("SELECT * FROM manuals")
            library = [row for row in cursor]
        except Exception as exc:
            print("Houve um erro ao recuperar informações do bando de dados.")
            print("Código do erro", exc)
        finally:
            self.cur.close()
            self.conn.commit()
        return library

    def list_manual(self, data_id):
        """List all chapters and attachments of a manual."""
        try:
            data = (data_id,)
            self.cur = self.conn.cursor()
            cursor = self.cur.execute("SELECT * FROM documentos WHERE manual_id = ? ORDER BY ordem", data)
            library = [row for row in cursor]
        except Exception as exc:
            print("Houve um erro ao recuperar informações do bando de dados.")
            print("Código do erro", exc)
        finally:
            self.cur.close()
            self.conn.commit()
        return library

    def update_link(self, link):
        """Update the link of the library, if it change."""
        try:
            desc = "link-normas"
            data = (link, desc)
            self.cur = self.conn.cursor()
            self.cur.execute("UPDATE information SET informacao = ? WHERE descricao = ?", data)
        except Exception as exc:
            print("Houve um erro ao atualizar o bando de dados.")
            print("Código do erro", exc)
            print("O banco de dados não foi atualizado.")
            return False
        finally:
            self.cur.close()
            self.conn.commit()
        return "Banco de dados atualizado com sucesso"

    def consult_link(self):
        """Return the link of library."""
        try:
            self.cur = self.conn.cursor()
            cursor = self.cur.execute("SELECT informacao FROM information WHERE descricao='link-normas'")
            link = cursor.fetchone()
        except Exception as exc:
            print("Houve um erro ao consultar o bando de dados.")
            print("Código do erro", exc)
            return False
        finally:
            self.cur.close()
        return link[0]

    def close_db(self):
        """Close a connection with DB."""
        self.conn.close()
        return "Conexão Fechada com sucesso."
