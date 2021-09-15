import socket
import threading
from editor import codeEditor

class client:
    def __init__(self,serverIP,serverPort):
        self.mainCodeInTextEditor=""
        self.username=""
        self.getUsername()
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((serverIP,serverPort))

        self.recieveCodeAndChat_thread = threading.Thread(target=self.recieveCodeAndChat)
        self.recieveCodeAndChat_thread.start()

        self.clientEditor=codeEditor()
        self.clientEditor.getCodeVarInEditorObj().trace('w',self.realTimeCodeChanged)
        self.clientEditor.getSendChatButton()['command']=self.sendChatClicked
        self.clientEditor.startCodeEditor()

    def recieveCodeAndChat(self):
        while True:
            try:
                message = self.client.recv(1024).decode("ascii")
                if message == "____USER____NAME____":
                    self.client.send(self.username.encode("ascii"))
                else:
                    message=str(message)
                    message=message.split(" ",1)
                    if message[1][:14]=="@@USER@@CHAT@@":
                        message=message[1][14:]
                        self.clientEditor.insertNewChatInchatDisplay("\n"+message)
                    else:
                        if message[0]!=self.username:
                            message=message[1]
                            self.mainCodeInTextEditor=str(message)
                            self.clientEditor.deleteAllTextInCode()
                            self.clientEditor.insertNewCodeInCode(self.mainCodeInTextEditor)
            except:
                print("\nAn error occured!...\n")
                self.client.close()
                break

    def realTimeCodeChanged(self,*args,**kwargs):
        self.mainCodeInTextEditor=str(self.clientEditor.getCodeVarInEditorObj().get())
        self.client.send(self.mainCodeInTextEditor.encode("ascii"))

    def getUsername(self):
        self.username=input("Enter your name: ")

    def sendChatClicked(self):
        input_given = self.clientEditor.chatInput.get(1.0,"end-1c")
        message = "@@USER@@CHAT@@"+str(self.username)+"> "+input_given
        self.clientEditor.deleteChatInChatInput()
        self.client.send(message.encode("ascii"))
        
        

if __name__ == "__main__":
    HOST_IP = "127.0.0.1"
    HOST_PORT = 11111
    c = client(HOST_IP,HOST_PORT)