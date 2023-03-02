#!/usr/bin/env python3
"""Module to create user interface."""


class UI:
    """Create user interface in terminal, without GUI."""

    def __init__(self, title):
        """Create a object UI (user interface)."""
        self.title = title

    def line(self, tam=70):
        """Print a line in UI."""
        return '-' * tam

    def header(self):
        """Create header for UI."""
        print('=' * 70)
        print(str.center(self.title, 70))
        print('=' * 70)
        print("\n")

    def menu(self, options):
        """Create menu for UI."""
        num = 1
        for item in options:
            print(f'[ {num} ] - {item}')
            num += 1
        print(self.line())
        option = input('Sua opção:  ')
        return option
