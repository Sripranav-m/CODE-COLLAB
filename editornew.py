import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, LEFT, RIGHT, TOP
from tkinter.scrolledtext import ScrolledText

class codeEditor:
    def __init__(self):
        self.screen = tk.Tk(className='Collaborative Coding')
        firstFrame = tk.Frame(self.screen)
        self.MainHeading = tk.Label(firstFrame, text="Collaborative editor")
        self.paticipantList = ScrolledText(firstFrame)
        firstFrame.pack(fill="x")
        self.MainHeading.pack(fill="x", side=LEFT)
        self.paticipantList.pack(fill='x', side=RIGHT, expand=True)

        secondFrame = tk.Frame(self.screen)
        self.editorLabel = tk.Label(secondFrame, text="Write code here")
        self.editorPanel = ScrolledText(secondFrame)
        secondFrame.pack(fill='x')
        self.editorLabel.pack(fill =BOTH, expand=True ,side = TOP)
        self.editorPanel.pack(fill=BOTH, expand = True)

        thirdFrame = tk.Frame(self.screen)
        self.chatLabel = tk.Label(thirdFrame, text="Chat is Here")
        self.chatPanel = ScrolledText(thirdFrame)
        thirdFrame.pack(fill='x')
        self.chatLabel.pack(fill = 'x', side = TOP)
        self.chatPanel.pack(fill=BOTH, expand = True)

        forthFrame = tk.Frame(self.screen)
        self.chatTypeBox = tk.Text(forthFrame)
        forthFrame.pack(fill='x')
        self.chatSendButton = tk.Button(forthFrame, text = "send")
        self.chatSendButton.pack(fill = 'x', side = RIGHT, expand=False)
        self.chatTypeBox.pack(fill=BOTH, expand=True)
        self.screen.geometry("600x400")
        self.screen.mainloop()


if __name__ == "__main__":
    c = codeEditor()