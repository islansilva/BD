from socket import *


class controlSend():
    def __init__(self, con):
        self.conSocket = con
    
    def send(self, msg):
        msgSend = str(msg).encode('UTF-8')
        self.conSocket.send(msgSend)