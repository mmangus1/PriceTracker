#!/usr/bin/env python

"""
Price Checker Python GUI
"""

import tkinter
import tkinter.messagebox

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

        App(root).pack()
        root.mainloop()

    except Exception as e:
        tkinter.messagebox.showerror(f'Error: {e}')



if __name__ == "__main__":
    main()
