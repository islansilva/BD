from os import chmod
from socket import *
from threading import Thread
from datetime import datetime
from funcoes.login import Login

class ControlRequest():
    
    def __init__(self, server):
        self.server = server
        self.run()


    def run(self):
        while True:
            connectionSocket, addr = self.server.serverSocket.accept()

            #informações da conexão
            """ print("Cliente {} conectado ao servidor".format(connectionSocket, addr)) """

            Thread(target=Login, args=(connectionSocket,)).start()