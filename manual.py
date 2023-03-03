#!/usr/bin/env python3
"""Class for manual object."""


class Manual:
    """Create a manual object."""

    def __init__(self, indice):
        """Create a object with chapters and attachments."""
        self.indice = indice

    def list_chapters(self):
        """List a index with chapters."""
        pass

    def download_manual(self):
        """Download the entire manual."""
        pass

    def download_chapter(self, chapter):
        """Download the specific chapter."""
        pass