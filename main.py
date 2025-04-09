import tkinter
import tkinter.messagebox


class App(tkinter.Frame):
    def __init__(self, parent, *args, **kwargs):
        '''

        :param parent:
        :param args:
        :param kwargs:
        '''
        super().__init__()
        self.parent = parent

def main():
    '''

    :return:
    '''
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


        App(root).pack()
        root.mainloop()

    except Exception as E:
        tkinter.messagebox.showerror(f'Error: {E}')



if __name__ == "__main__":
    main()
