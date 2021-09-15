import socket
import threading
from editor import codeEditor



class client:
    def __init__(self,serverIP,serverPort):
        self.username=""
        self.getUsername()
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((serverIP,serverPort))

        self.clientEditor=codeEditor()
        # The 'w' mode will automatically invoke the callback whenever the value of the Code_Var changes.
        self.clientEditor.Code_Var.trace('w',self.realTimeCodeChanged)

        self.receive_thread = threading.Thread(target=self.recieve)
        self.receive_thread.start()

        self.write_thread = threading.Thread(target=self.write)
        self.write_thread.start()


    def recieve(self):
        while True:
            try:
                # Recieving the message
                message = self.client.recv(1024).decode("ascii")
                if message == "__USERNAME__":
                    # Send the username
                    self.client.send(self.username.encode("ascii"))
                else:
                    print(message)
            except:
                print("An error occured! ")
                self.client.close()
                break

    def write(self):
        while True:
            # Entering the message
            message = str(self.username)+"> "+input("")
            self.client.send(message.encode("ascii"))

    def realTimeCodeChanged(self,*args,**kwargs):
        print(self.clientEditor.Code_Var.get())


    def getUsername(self):
        self.username=input("Enter your name: ")
        

if __name__ == "__main__":
    HOST_IP = "127.0.0.1"
    HOST_PORT = 11111
    c = client(HOST_IP,HOST_PORT)