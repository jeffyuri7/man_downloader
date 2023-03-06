#!/usr/bin/env python3
"""A class module of documents of a manual."""

import requests
import os


class Document:
    """Specify a document of a manual."""

    def __init__(self, id_document, title, link, manual_id):
        """Build a document object."""
        self.id = id_document  # ID of document in database
        self.title = title  # Title of document
        self.link = link  # Link to download the document
        self.manual_id = manual_id  # Foreign key of manual.

    def download_document(self, folder):
        """Download DOC from URL to local directory.

        :param url: The url of the DOC file to be downloaded
        :return: True if DOC file was successfully downloaded, otherwise False.
        """
        # Request URL and get response object
        response = requests.get(self.link, stream=True)

        # isolate DOC filename from URL
        doc_file_name = os.path.basename(self.link)
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

    def update_document(self, id, title, link, manual_id):
        """Update a document information."""
        self.id = id
        self.title = title
        self.link = link
        self.manual_id = manual_id

if __name__ == '__main__':
    documento = Document(2, "Capítulo 1", "https://intranet.correios.com.br/ect-normas/manafi/copy_of_MANAFIMODULO05CAPTULO001_Anexo01.doc", 2)
    documento.download_document()
