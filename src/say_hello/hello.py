#!/usr/bin/env python3


class Printer:
    """the attributes of the Printer class are
    * ink_level: the current amount of ink in the printer
    * paper_level: the current amount of paper in the printer
    """
    def __init__(self, ink_level, paper_level):
        self.ink_level = ink_level
        self.paper_level = paper_level


    def print_document(self, pages):
        """Print a document with the specified number of pages."""
        if pages > self.paper_level:
            print(f"Not enough paper to print {pages} pages.")
            return

        print(f"Printing {pages} pages...")
        self.paper_level -= pages
        self.ink_level -= pages * 0.5  # Assuming each page uses 0.5% ink

        self.check_status() # call the next method, check_status

    def check_status(self):
        """Check printer status and notify if needed."""
        self.notify_low_ink() # call the next method, notify_low_ink
        self.notify_out_of_paper() # call the next method, notify_out_of_paper

    def notify_low_ink(self):
        """Notify if ink level is low."""
        if self.ink_level <= 10:
            print("Warning: Ink is low.")
        else:
            print(f"Ink level: {self.ink_level}%")

    def notify_out_of_paper(self):
        """Notify if paper is low or out."""
        if self.paper_level == 0:
            print("Error: Printer is out of paper.")
        elif self.paper_level <= 10:
            print(f"Warning: Low on paper. Only {self.paper_level} sheets remaining.")
        else:
            print(f"Paper remaining: {self.paper_level} sheets")


if __name__ == "__main__":
    """
     Direct execution example (for testing this module independently).

     Note: In production, this class is instantiated and used via main.py.
     The __init__.py exposes this class for import by other modules.

     Test the Printer class directly by uncommenting the code below.
     """
    # Example usage:
    # hp = Printer(ink_level=100, paper_level=50)
    #
    # print("Initial printer status:")
    # hp.check_status()
    #
    # print("\nPrinting 33 pages:")
    # hp.print_document(33)
    #
    # print("\nPrinting 20 more pages:")
    # hp.print_document(20)