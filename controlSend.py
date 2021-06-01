from socket import *


class controlSend():
    def __init__(self, con):
        self.conSocket = con
    
    
    def send(self, msg):
        msgSend = str(msg).encode('latin-1')
        self.conSocket.send(msgSend)