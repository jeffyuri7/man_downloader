#!/usr/bin/env python3
"""A class module of documents of a manual."""


class Document:
    """Specify a document of a manual."""

    def __init__(self, id, title, link, manual_id):
        """Build a document object."""
        self.id = id
        self.title = title
        self.link = link
        self.manual_id = manual_id

    def show_document(self):
        """Show information about a document."""
        pass

    def download_document(self):
        """Download a document of specific manual."""
        pass

    def update_document(self, id, title, link, manual_id):
        """Update a document information."""
        self.id = id
        self.title = title
        self.link = link
        self.manual_id = manual_id
