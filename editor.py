from tkinter import *

class codeEditor:
    def __init__(self):
        self.screen = Tk(className='Collaborative Coding')
        self.screen.geometry("500x200")
        self.Code_Var = StringVar()
        self.Code_Entry = Entry(self.screen,textvariable=self.Code_Var)
        self.Code_Entry.pack()
        # The 'w' mode will automatically invoke the callback whenever the value of the Code_Var changes.

        self.screen.mainloop()


if __name__ == "__main__":
    c = codeEditor()