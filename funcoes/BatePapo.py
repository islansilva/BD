from controlSend import controlSend
from funcoes.colors import Cor
import settings
import os
import sys
import time

sys.path.append(os.path.abspath("../BatePapo"))


class BatePapo:

    def __init__(self, userData):
        self.conexao = userData
        self.salaLogado = ""

    @staticmethod
    def createRoom():

        # 0 =  Nome
        # 1 =  Sockets
        arrRoom = [['Futebol', [], []], ['Namoro', [], []], ['Carros', [], []]]

        return arrRoom

    def commands(self):
        exibeComando = f"""\r
{Cor.vermelho}ENTER{Cor.reset} \t\t INGRESSAR NA SALA \r
{Cor.vermelho}CHAT{Cor.reset} \t\t ENVIAR MENSAGEM \r
{Cor.vermelho}ONLINE{Cor.reset} \t\t VERIFICAR USUARIOS ONLINE \r
{Cor.vermelho}ROOMS{Cor.reset} \t\t SALAS EXISTENTES \r
{Cor.vermelho}CREATEROOMS{Cor.reset} \t CRIAR NOVAS SALAS DE BATE PAPO \r
{Cor.vermelho}EXITROOMS{Cor.reset} \t SAIR DA SALA \r
{Cor.vermelho}QUIT{Cor.reset} \t\t ENCERRA A CONEXAO E SAI DO BATE PAPO \r
{Cor.vermelho}HELP{Cor.reset} \t\t PARA LISTAR OS COMANDOS \r\n"""

        return exibeComando

    def broadcast(self, clients, msg):

        for sock in clients:
            if sock != self.conexao.conSocket:
                enviamsg = controlSend(sock)
                enviamsg.send("\r" + str(msg))

    def inputCommand(self, inputText):

        print(settings.rooms)
        splitTexto = inputText.split(" ")
        print(splitTexto)

        if splitTexto[0] == 'ENTER':
            # VERIFICA SE A SALA EXISTE
            for i in range(len(settings.rooms)):

                campoProc = splitTexto[1].replace('\r\n', "").strip()
                if campoProc == settings.rooms[i][0]:
                    self.salaLogado = campoProc
                    self.broadcast(settings.rooms[i][1], str(
                        self.conexao.infoUser['nameAlias']) + " entrou na sala\r\n")

                    settings.rooms[i][1].append(self.conexao.conSocket)
                    settings.rooms[i][2].append(
                        self.conexao.infoUser['nameAlias'])
                    self.conexao.controlSend.send("\rIngressando na sala...")
                    time.sleep(2)
                    return f"\r\n{Cor.verde}Tudo OK !!!{Cor.reset} \r\n"

            return "\rSALA INEXISTENTE\r\n"
        elif splitTexto[0] == "CHAT":

            if self.salaLogado == "":
                return "\rEntre em uma sala para enviar msg...\r\n"

            for i in range(len(settings.rooms)):

                if self.salaLogado == settings.rooms[i][0]:
                    self.broadcast(
                        settings.rooms[i][1], self.conexao.infoUser['nameAlias'] + ": " + str(" ".join(splitTexto[1:])))
                    return ""

        elif splitTexto[0] == "ONLINE":
            if self.salaLogado == "":
                return "\rEntre em uma sala para verificar usuarios online...\r\n"
            
            users = "Usuarios online:\r\n-> "

            for i in range(len(settings.rooms)):
                if settings.rooms[i][0]== self.salaLogado:
                    print(settings.rooms[i][2])
                    users += '\r\n-> '.join(settings.rooms[i][2])
            users += "\r\n"
            return users

        elif splitTexto[0] == "ROOMS":
            salas = ""

            for i in range(len(settings.rooms)):
                salas += settings.rooms[i][0] + "\r\n"

            return salas

        elif splitTexto[0] == "CREATEROOMS":

            sala = splitTexto[1].replace('\r\n', "").strip()

            if sala == "":
                return "\rInforme o nome de uma sala\r\n"

            settings.rooms.append([sala, [], []])

        else:
            return "\rCOMANDO NAO DISPONIVEL\r\n"
