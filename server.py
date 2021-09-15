import socket
import threading

class server:
    def __init__(self,serverIP,serverPort):
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((HOST_IP,HOST_PORT))
        self.server.listen()

        self.clients = []
        self.usernames=[]

        print("Server Started...\n")
        self.recieve()

    def broadcast(self,message):
        for client in self.clients:
            client.send(message.encode("ascii"))

    def handle(self,client):
        while True:
            try:
                message=client.recv(1024).decode()
                message=str(message)
                index = self.clients.index(client)
                message=self.usernames[index]+" "+message
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                username=self.usernames[index]
                self.usernames.remove(username)
                break

    def recieve(self):
        while True:
            client,address = self.server.accept()
            print("Connected with "+str(address))
            client.send("____USER____NAME____".encode('ascii'))
            username=client.recv(1024).decode("ascii")
            self.usernames.append(username)
            self.clients.append(client)
            print("Username of the client is: "+str(username)+"\n\n\n")
            client.send((str(username)+" Connected to the server...\n\n").encode("ascii"))

            thread=threading.Thread(target=self.handle,args=(client,))
            thread.start()


if __name__ == "__main__":
    HOST_IP = "127.0.0.1"
    HOST_PORT = 11111
    s=server(HOST_IP,HOST_PORT)