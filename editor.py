import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class codeEditor:
    def __init__(self):
        self.screen = tk.Tk(className='Collaborative Coding')
        self.screen.geometry("500x500")
        self.Code_Var = tk.StringVar()
        self.codeScrolledText = ScrolledText(self.screen)
        self.codeScrolledText.pack()
        self.codeScrolledText.bind('<KeyRelease>', self.get_stringvar)

    def get_stringvar(self,event):
        self.Code_Var.set(self.codeScrolledText.get("1.0", tk.END))

    def startCodeEditor(self):
        self.screen.mainloop()

    def getCodeVarInEditorObj(self):
        return self.Code_Var

    def getScrolledText(self):
        return self.codeScrolledText

if __name__ == "__main__":
    c = codeEditor()