#!/usr/bin/env python

"""
Price Checker Python GUI
"""

import tkinter
import tkinter.messagebox
import smtplib
from typing import AnyStr

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
        super().__init__()
        self.parent = parent


def search(productcode: str,itemsearch: str) -> tuple[str,str]:

    # Set User Agent of Browser:
    header = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/44.0.2403.157 Safari/537.36',
                             'Accept-Language': 'en-US, en;q=0.5'})

    if (productcode != None or productcode != ""):
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
        walmart_price = (walmart_soup.find("span", attrs={'id': 'priceblock_ourprice'})
                 .string.strip().replace(',', ''))

    except AttributeError:
        walmart_price = "NA"

    # Amazon Price Retrieval:
    try:
        amazon_price = (amazon_soup.find("span", attrs={'id': 'priceblock_ourprice'})
                         .string.strip().replace(',', ''))

    except AttributeError:
        amazon_price = "NA"

    # Must find code to bypass captcha's and anti bots, remove bugs from unsanitized inputs, set prices to text boxes.

    return walmart_price, amazon_price


def main() -> None:
    """Create the main function, mainly to handle errors in the proceeding code.

    Keyword Arguments:
    None
    """
    try:
        # Main GUI Window Set Up:
        root = tkinter.Tk()
        root.geometry('1024x768')
        root.title('Price Tracker')
        menubar = tkinter.Menu(root)
        root.config(menu=menubar)

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
            command=root.destroy,
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

        # Item Search Label:
        item_search_label = tkinter.Label(root, text="Individual Item Search:")

        # Item Search Label Placement:
        item_search_label.place(x=20,y=20)

        # Item Search Textbox:
        item_search_textbox = tkinter.Text(root, height=1, width=20)

        # Item Search Textbox Placement:
        item_search_textbox.place(x=150,y=20)

        # Or Label:
        or_label = tkinter.Label(root, text="OR")

        # Or Label Placement:
        or_label.place(x=150,y=47)

        # Item Code Label:
        productcode_label = tkinter.Label(root, text="Item Code:")

        # Item Code Label Placement:
        productcode_label.place(x=63,y=75)

        # Item Code Textbox:
        productcode_textbox = tkinter.Text(root, height=1, width=20)

        # Item Code Textbox Placement:
        productcode_textbox.place(x=150, y=75)

        # Individual Search Button:
        individual_search_button = tkinter.Button(root, text="Search", command=search(productcode=productcode_textbox.get("1.0", tkinter.END),itemsearch=item_search_textbox.get("1.0", tkinter.END)))

        # Individual Search Button Placement:
        individual_search_button.place(x=350, y=47)

        # Prices Label:
        prices_label = tkinter.Label(root, text="Prices:")

        # Prices Label Placement:
        prices_label.place(x=600,y=10)

        # Amazon.com Label:
        amazon_label = tkinter.Label(root, text="Amazon.com:")

        # Amazon.com Label Placement:
        amazon_label.place(x=500,y=40)

        # Amazon.com Textbox:
        amazon_textbox = tkinter.Text(root, height=1, width=25)

        # Amazon.com Textbox Placement:
        amazon_textbox.place(x=600,y=40)

        # Walmart.com Label:
        walmart_label = tkinter.Label(root, text="Walmart.com:")

        # Walmart.com Label Placement:
        walmart_label.place(x=500,y=80)

        # Walmart Textbox:
        walmart_textbox = tkinter.Text(root, height=1, width=25)

        # Walmart Textbox Placement:
        walmart_textbox.place(x=600,y=80)

        App(root).pack()
        root.mainloop()

    except Exception as e:
        tkinter.messagebox.showerror(f'Error: {e}')



if __name__ == "__main__":
    main()
