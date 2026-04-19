#!/usr/bin/env python3

# look in the `src/say_hello/__init__.py` package
# __init__.py acts as the package's entry point'
# src is the dir, say_hello.py is the file, Printer is the class
from src.say_hello import Printer

"""
    # How to Create an instance of the printer object
    hp = Printer()

    # How to test the printer methods
    print("Initial printer status:")
    hp.check_status()

    print("\nPrinting 33 pages:")
    hp.print_document(33)

    print("\nPrinting 20 more pages:")
    hp.print_document(20)

"""

def print_hello():
    print("Hello, Object-Oriented Programming!")



def main():
    # This is where the Printer Object is Created. AKA instance of the Printer Class
    printer = Printer(100, 100)
    print_hello()

    print("\nInitial printer status:")
    printer.check_status()

    print("\nPrinting 33 pages:")
    printer.print_document(33)

    print("\nPrinting 20 more pages:")
    printer.print_document(20)


if __name__ == "__main__":
    main()

