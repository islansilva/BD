from socket import *
from datetime import datetime
from controlRequest import ControlRequest
from funcoes.BatePapo import BatePapo
import settings

class Server:
    def __init__(self, ip, port):
        currentTime = datetime.now()
        d = currentTime.ctime()
        date_array = d.split()
        data_formatada = f'Date: {date_array[0]}, {d[4:]} BRT\r\n'

        self.ip = ip
        self.port = port

        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serverSocket.bind((self.ip, self.port))
        serverSocket.listen(1)


        settings.rooms = BatePapo.createRoom();
        print(settings.rooms)


        #self.connectionSocket = connectionSocket
        #self.addr = addr

        self.serverSocket = serverSocket
        self.data = data_formatada


        self.ControlRequest = ControlRequest(self)
        #self.ControlRequest.start()