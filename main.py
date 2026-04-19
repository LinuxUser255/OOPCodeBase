#!/usr/bin/env python3
"""
OOP demo entry point.

Demonstrates instantiation and usage of the Printer class.

Package layout:
    src/say_hello/__init__.py  -- package entry point
    Printer                    -- the class imported below

Usage:
    python main.py

Example:
    hp = Printer(100, 100)
    hp.check_status()
    hp.print_document(33)
    hp.print_document(20)
"""

from src.say_hello import Printer


INITIAL_PAGE_CAPACITY = 100
INITIAL_INK_LEVEL = 100


def print_hello() -> None:
    """Print the OOP greeting message."""
    print("Hello, Object-Oriented Programming!")


def main() -> None:
    """Run the Printer demo."""
    printer = Printer(INITIAL_PAGE_CAPACITY, INITIAL_INK_LEVEL)
    print_hello()

    print("\nInitial printer status:")
    printer.check_status()

    print("\nPrinting 33 pages:")
    printer.print_document(33)

    print("\nPrinting 20 more pages:")
    printer.print_document(20)


if __name__ == "__main__":
    main()

