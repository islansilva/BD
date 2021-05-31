import sys
from socket import *
from funcoes.colors import Cor

from controlSend import controlSend

class BatePapo:
    

    def __init__(self, userData):
        self.cores = Cor()
        self.userData = userData
        pass


    @staticmethod
    def createRoom():

        #0 =  Nome
        #1 =  Sockets
        arrRoom = [['Futebol', []], ['Namoro', []], ['Carros', []]]

        return arrRoom

    def commands(self):

        exibeComando = f"""\r
{self.cores.vermelho}INSERT {self.cores.reset}\t\t ENVIAR MENSAGEM \r
{self.cores.vermelho}ONLINE {self.cores.reset}\t\t VERIFICAR USUARIOS ONLINE \r
{self.cores.vermelho}ROOMS {self.cores.reset}\t\t SALAS EXISTENTES \r
{self.cores.vermelho}CREATEROOMS {self.cores.reset}\t CRIAR NOVAS SALAS DE BATE PAPO \r
{self.cores.vermelho}ENTERROOMS {self.cores.reset}\t ENTRAR EM UMA SALA \r
{self.cores.vermelho}EXITROOMS {self.cores.reset}\t SAIR DA SALA \r
{self.cores.vermelho}QUIT {self.cores.reset}\t\t ENCERRA A CONEXAO E SAI DO BATE PAPO \r
{self.cores.vermelho}HELP {self.cores.reset}\t\t PARA LISTAR OS COMANDOS \r\n"""
        return exibeComando


        
    def inputCommand(self, inputText):

        dispCommands = ['INSERT', 'ONLINE', 'ROOMS', 'CREATEROOMS', 'ENTERROOMS', 'EXITROOMS', 'QUIT', 'HELP']


        splitTexto = inputText.split(" ")

        if not splitTexto[0] in dispCommands:
            ret = "COMANDO NÃO DISPONÍVEL"
