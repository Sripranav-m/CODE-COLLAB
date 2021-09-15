import socket
import threading
from editor import codeEditor
import tkinter as tk

class client:
    def __init__(self,serverIP,serverPort):
        self.mainCodeInTextEditor=""
        self.username=""
        self.getUsername()
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((serverIP,serverPort))

        self.receive_thread = threading.Thread(target=self.recieve)
        self.receive_thread.start()

        self.clientEditor=codeEditor()
        self.clientEditor.getCodeVarInEditorObj().trace('w',self.realTimeCodeChanged)
        self.clientEditor.startCodeEditor()

    def recieve(self):
        while True:
            try:
                message = self.client.recv(1024).decode("ascii")
                if message == "____USER____NAME____":
                    self.client.send(self.username.encode("ascii"))
                else:
                    message=str(message)
                    message=message.split(" ",1)
                    if message[0]!=self.username:
                        message=message[1]
                        self.mainCodeInTextEditor=str(message)
                        self.clientEditor.getScrolledText().delete("1.0",tk.END)
                        self.clientEditor.getScrolledText().insert(tk.INSERT,self.mainCodeInTextEditor)
                        print(self.mainCodeInTextEditor)
            except:
                print("\nAn error occured!...\n")
                self.client.close()
                break

    def realTimeCodeChanged(self,*args,**kwargs):
        self.mainCodeInTextEditor=str(self.clientEditor.getCodeVarInEditorObj().get())
        self.client.send(self.mainCodeInTextEditor.encode("ascii"))

    def getUsername(self):
        self.username=input("Enter your name: ")
        

if __name__ == "__main__":
    HOST_IP = "127.0.0.1"
    HOST_PORT = 11111
    c = client(HOST_IP,HOST_PORT)