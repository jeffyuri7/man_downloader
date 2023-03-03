#!/usr/bin/env python3
"""Module to create user interface."""

from time import sleep
from utils.helper import clear


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
        option = self.inputInt('Sua opção:  ')
        return option

    def inputInt(self, choice):
        """Read and converte user's choice to int."""
        while True:
            try:
                num = int(input(choice))
            except (ValueError, TypeError):
                return None
            except (KeyboardInterrupt):
                return None
            else:
                return num

    def exitTo(self):
        """Exit of program."""
        print("\nSaindo do programa...\n")
        sleep(1)
        print('VOLTE SEMPRE QUE PRECISAR!\n')
        sleep(3)
        return None

    def menu_manuals(self, options):
        """Create a menu with the manuals."""
        lista = []
        num = 1
        for key, value in options.items():
            print(f'[ {str.center(str(num), 4)} ] - {key} ')
            num += 1
            lista.append(key)
        print(self.line())
        option = self.inputInt('Sua opção:  ')
        return lista[option-1]
