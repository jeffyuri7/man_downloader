#!/usr/bin/env python3
"""This module include the logical about database."""

import sqlite3


class DB:
    """Create a database object."""

    def __init__(self):
        """Create a database object."""
        self.conn = sqlite3.connect('database.sqlite3')

    def insert(self):
        """Insert data to the database."""
        pass

    def update(self):
        """Update the database."""
        pass

    def select(self):
        """Select data in database."""
        pass

    def update_link(self, link):
        """Update the link if it change."""
        pass
