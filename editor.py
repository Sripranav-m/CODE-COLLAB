import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from time import sleep

class codeEditor:
    def __init__(self):
        self.screen = tk.Tk(className='{COLLABORATIVE CODING WITH CHAT}')
        self.createMainHeadingAndShowCurrentUSers()
        self.createCodeSection()
        self.createChatDisplay()
        self.createChatTypeandSendBtn()
        self.screen.geometry("742x860")
        self.screen.resizable(False, False)

    def addUserName(self,username):
        self.MainHeading['text']="Welcome to COLLAB,"+username

    def createMainHeadingAndShowCurrentUSers(self):
        self.firstFrame = tk.Frame(self.screen, relief=tk.RAISED, bd=2,height=3)

        self.MainHeading = tk.Label(self.firstFrame,height=3,width=62)
        self.MainHeading.grid(row=0,column=0)
        self.MainHeading['text']="Welcome to COLLAB , User"
        self.MainHeading.configure(state="disabled")
        self.MainHeading.config(fg="#000000")
        self.MainHeading.config(bg="lightgreen")

        self.ShowCurrentUsers = ScrolledText(self.firstFrame,height=3,width=35)
        self.ShowCurrentUsers.grid(row=0,column=1,sticky= "nsew")
        self.ShowCurrentUsers.configure(state="disabled")

        self.firstFrame.grid(row=0, column=0, sticky="nsew")

    def createCodeSection(self):
        self.secondFrame = tk.Frame(self.screen, relief=tk.RAISED, bd=2)
        self.Code_Var = tk.StringVar()

        self.editorLable = tk.Label(self.secondFrame)
        self.editorLable.grid(row=0,column=0, sticky="nsew")
        self.editorLable['text'] = 'COLLABORATIVE CODING PAD'
        self.editorLable.configure(state="disabled")
        self.editorLable.config(font=("Courier bold",10))
        self.editorLable.config(fg="#000000")
        self.editorLable.config(bg="lightblue")

        self.codeScrolledText = ScrolledText(self.secondFrame,height=33,width=90)
        self.codeScrolledText.grid(row=1,column=0, sticky="nsew")
        self.codeScrolledText.bind('<KeyRelease>', self.get_stringvar)

        self.secondFrame.grid(row=1, column=0, sticky="nsew")

    def createChatDisplay(self):
        self.thirdFrame = tk.Frame(self.screen, relief=tk.RAISED, bd=2)

        self.chatDisplayLabelAll = tk.Label(self.thirdFrame)
        self.chatDisplayLabelAll.grid(row=0,column=0,  sticky="nsew")
        self.chatDisplayLabelAll['text'] = 'ALL CHATS ARE VISIBLE HERE'
        self.chatDisplayLabelAll.configure(state="disabled")
        self.chatDisplayLabelAll.config(font=("Courier bold",10))
        self.chatDisplayLabelAll.config(fg="#000000")
        self.chatDisplayLabelAll.config(bg="lightblue")

        self.chatDisplay = ScrolledText(self.thirdFrame,height=10,width=90)
        self.chatDisplay.grid(row=1,column=0, sticky="nsew")
        self.chatDisplay.configure(state="disabled")

        self.thirdFrame.grid(row=2, column=0, sticky="nsew")

    def createChatTypeandSendBtn(self):
        self.fourthFrame = tk.Frame(self.screen, relief=tk.RAISED, bd=2)

        self.chatDisplayLabel = tk.Label(self.fourthFrame)
        self.chatDisplayLabel.grid(row=0,column=0,sticky="nsew")
        self.chatDisplayLabel['text'] = 'ENTER YOUR CHAT'
        self.chatDisplayLabel.configure(state="disabled")
        self.chatDisplayLabel.config(font=("Courier bold",10))
        self.chatDisplayLabel.config(fg="#000000")
        self.chatDisplayLabel.config(bg="lightblue")

        buttonFram = tk.Frame(self.fourthFrame, relief=tk.RAISED, bd=2)

        self.chatSendBtn = tk.Button(buttonFram, text="Send",width=15,background="lightgreen")
        self.chatInput = tk.Text(buttonFram,height=1,width=77)
        self.chatInput.grid(row=0,column=0, sticky="nsew")
        self.chatSendBtn.grid(row=0, column=1, sticky="nsew")

        buttonFram.grid(row=1, column=0, sticky="nsew")

        self.fourthFrame.grid(row=3, column=0, sticky="nsew")

    def get_stringvar(self,event):
        self.Code_Var.set(self.codeScrolledText.get("1.0", tk.END))

    def enterNewUserNames(self,usernames):
        print(usernames)
        self.ShowCurrentUsers.configure(state="normal")
        self.ShowCurrentUsers.delete("1.0",tk.END)
        for user in usernames:
            self.ShowCurrentUsers.insert(tk.END,user+"\n")
        self.ShowCurrentUsers.configure(state="disabled")

    def startCodeEditor(self):
        self.codeScrolledText.config(state=tk.NORMAL)
        self.screen.mainloop()

    def deleteAllTextInCode(self):
        self.codeScrolledText.delete("1.0",tk.END)

    def insertNewChatInchatDisplay(self,newChat):
        self.chatDisplay.configure(state="normal")
        self.chatDisplay.insert(tk.END,newChat)
        self.chatDisplay.configure(state="disabled")

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
    c.startCodeEditor()