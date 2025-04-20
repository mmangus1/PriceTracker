#!/usr/bin/env python

"""
Price Checker Python GUI
"""

import tkinter
import tkinter.messagebox
import smtplib
from typing import AnyStr
# import solvecaptcha # Looks like this is the module I'll use
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price

__author__ = "Matthew Mangus"
__copyright__ = "Copyright 2025, Matthew Mangus"
__credits__ = ["Matthew Mangus"]
__license__ = "The Unlicense"
__version__ = "1.0.1"
__maintainer__ = "Matthew Mangus"
__email__ = "mmangus1@student.montcalm.edu"
__status__ = "Development"


class App(tkinter.Frame):
    """Create a Tkinter Window GUI.

    Keyword Arguments:
    tkinter.frame = tkinter.frame instance argument
    """

    def __init__(self, parent, *args, **kwargs) -> None:
        """Create the initial method for App Class.

        Keyword Arguments:
        self =
        parent =
        *args =
        **kwargs =
        """
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.walmart_price = None
        self.amazon_price = None
        self.item_search_textbox = None  # Initialize these here
        self.productcode_textbox = None
        self.walmart_textbox = None
        self.amazon_textbox = None
        self.create_widgets()

    def search(self) -> None:
        """Perform the search for product prices."""
        productcode = self.productcode_textbox.get("1.0", tkinter.END).strip()
        itemsearch = self.item_search_textbox.get("1.0", tkinter.END).strip()

        # Set User Agent of Browser:
        header = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                'AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/44.0.2403.157 Safari/537.36',
                                'Accept-Language': 'en-US, en;q=0.5'})

        if productcode:
            search_query = productcode
        else:
            search_query = itemsearch

        # Walmart.com HTTP Request:
        walmart_search = requests.get('https://www.walmart.com/search?q=' + search_query, headers=header)

        # Amazon.com HTTP Request:
        amazon_search = requests.get('https://www.amazon.com/s?k=' + search_query, headers=header)

        # Save Walmart Webpage Data:
        walmart_soup = BeautifulSoup(walmart_search.content, 'lxml')

        # Save Amazon Webpage Data:
        amazon_soup = BeautifulSoup(amazon_search.content, 'lxml')

        # Walmart Price Retrieval:
        try:
            walmart_price = (walmart_soup.find("span", attrs={'class': 'visually-hidden'})  # Changed attribute for more reliability
                    .string.strip().replace(',', ''))
            price_obj = Price(walmart_price)
            self.walmart_price = price_obj.amount_float
        except AttributeError:
            self.walmart_price = "NA"

        # Amazon Price Retrieval:
        try:
            amazon_price_element = amazon_soup.find("span", class_="a-offscreen")  # Using a more specific class
            if amazon_price_element:
                amazon_price = amazon_price_element.string.strip().replace(',', '')
                price_obj = Price(amazon_price)
                self.amazon_price = price_obj.amount_float
            else:
                self.amazon_price = "NA"
        except AttributeError:
            self.amazon_price = "NA"

        self.walmart_textbox.delete('1.0', tkinter.END)
        self.amazon_textbox.delete('1.0', tkinter.END)
        self.walmart_textbox.insert('1.0', self.walmart_price)
        self.amazon_textbox.insert('1.0', self.amazon_price)

    def create_widgets(self) -> None:
        """Create and place the widgets in the GUI."""
        # Item Search Label:
        item_search_label = tkinter.Label(self.parent, text="Individual Item Search:")
        item_search_label.place(x=20, y=20)

        # Item Search Textbox:
        self.item_search_textbox = tkinter.Text(self.parent, height=1, width=20)
        self.item_search_textbox.place(x=150, y=20)

        # Or Label:
        or_label = tkinter.Label(self.parent, text="OR")
        or_label.place(x=150, y=47)

        # Item Code Label:
        productcode_label = tkinter.Label(self.parent, text="Item Code:")
        productcode_label.place(x=63, y=75)

        # Item Code Textbox:
        self.productcode_textbox = tkinter.Text(self.parent, height=1, width=20)
        self.productcode_textbox.place(x=150, y=75)

        # Individual Search Button:
        individual_search_button = tkinter.Button(self.parent, text="Search", command=self.search)
        individual_search_button.place(x=350, y=47)

        # Prices Label:
        prices_label = tkinter.Label(self.parent, text="Prices:")
        prices_label.place(x=600, y=10)

        # Amazon.com Label:
        amazon_label = tkinter.Label(self.parent, text="Amazon.com:")
        amazon_label.place(x=500, y=40)

        # Amazon.com Textbox:
        self.amazon_textbox = tkinter.Text(self.parent, height=1, width=25)
        self.amazon_textbox.place(x=600, y=40)

        # Walmart.com Label:
        walmart_label = tkinter.Label(self.parent, text="Walmart.com:")
        walmart_label.place(x=500, y=80)

        # Walmart Textbox:
        self.walmart_textbox = tkinter.Text(self.parent, height=1, width=25)
        self.walmart_textbox.place(x=600, y=80)

    def main(self) -> None:
        """Create the main function, mainly to handle errors in the proceeding code.

        Keyword Arguments:
        None
        """
        try:
            # Main GUI Window Set Up:
            self.parent.geometry('1024x768')
            self.parent.title('Price Tracker')
            menubar = tkinter.Menu(self.parent)
            self.parent.config(menu=menubar)

            # "File" Menu:
            file_menu = tkinter.Menu(menubar, tearoff=0)

            # "File" Button:
            menubar.add_cascade(
                label="File",
                menu=file_menu,
            )

            # Dropdown Item #1 ("File" Button):
            file_menu.add_command(
                label='Exit',
                command=self.parent.destroy,
            )

            # "Edit" Menu:
            edit_menu = tkinter.Menu(menubar, tearoff=0)

            # "Edit" Button:
            menubar.add_cascade(
                label="Edit",
                menu=edit_menu,
            )

            # "Help" Menu:
            help_menu = tkinter.Menu(menubar, tearoff=0)

            # "Help" Button:
            menubar.add_cascade(
                label="Help",
                menu=help_menu,
            )

            # We've moved widget creation to create_widgets
            # App(self.parent).pack() # No need to create another App instance here
            self.pack()
            self.parent.mainloop()

        except Exception as e:
            tkinter.messagebox.showerror(f'Error: {e}')


if __name__ == "__main__":
    root = tkinter.Tk()  # Create the main window first
    app_instance = App(parent=root)  # Pass the root window to the App
    app_instance.main()