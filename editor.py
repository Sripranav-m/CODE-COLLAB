import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class codeEditor:
    def __init__(self):
        self.screen = tk.Tk(className='Collaborative Coding')
        self.createCodeSection()
        self.createChatDisplay()
        self.createChatTypeandSendBtn()
        self.screen.geometry("500x500")

    def createCodeSection(self):
        self.Code_Var = tk.StringVar()
        self.codeScrolledText = ScrolledText(self.screen, height= 10, width = 60)
        self.codeScrolledText.grid(row=0,column=0)
        self.codeScrolledText.bind('<KeyRelease>', self.get_stringvar)

    def createChatDisplay(self):
        self.chatDisplay = ScrolledText(self.screen, height = 7, width = 60)
        self.chatDisplay.grid(row=1,column=0, pady = 10)

    def createChatTypeandSendBtn(self):
        buttonFram = tk.Frame(self.screen, relief=tk.RAISED, bd=2, height=1, width=60)
        self.chatSendBtn = tk.Button(buttonFram, text="Send")
        self.chatInput = tk.Text(buttonFram, height = 1, width = 30)
        self.chatInput.grid(row=0,column=0)
        self.chatSendBtn.grid(row=0, column=1, sticky="ew")
        buttonFram.grid(row=2, column=0, sticky="ns",)


    def get_stringvar(self,event):
        self.Code_Var.set(self.codeScrolledText.get("1.0", tk.END))

    def startCodeEditor(self):
        self.codeScrolledText.config(state=tk.NORMAL)
        self.screen.mainloop()

    def deleteAllTextInCode(self):
        self.codeScrolledText.delete("1.0",tk.END)

    def insertNewChatInchatDisplay(self,newChat):
        self.chatDisplay.insert(tk.INSERT,newChat)

    def insertNewCodeInCode(self,newCode):
        self.codeScrolledText.insert(tk.INSERT,newCode)

    def deleteChatInChatInput(self):
        self.chatInput.delete("1.0",tk.END)

    def getCodeVarInEditorObj(self):
        return self.Code_Var

    def getScrolledText(self):
        return self.codeScrolledText

    def getSendChatButton(self):
        return self.chatSendBtn

if __name__ == "__main__":
    c = codeEditor()