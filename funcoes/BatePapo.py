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
        exibeComando = f"""-----------------------|-----------------------\r
{Cor.vermelho}ENTER{Cor.reset} \t\t INGRESSAR NA SALA \r
{Cor.vermelho}CHAT{Cor.reset} \t\t ENVIAR MENSAGEM \r
{Cor.vermelho}ONLINE{Cor.reset} \t\t VERIFICAR USUARIOS ONLINE \r
{Cor.vermelho}ROOMS{Cor.reset} \t\t SALAS EXISTENTES \r
{Cor.vermelho}CREATEROOMS{Cor.reset} \t CRIAR NOVAS SALAS DE BATE PAPO \r
{Cor.vermelho}EXITROOMS{Cor.reset} \t SAIR DA SALA \r
{Cor.vermelho}QUIT{Cor.reset} \t\t ENCERRA A CONEXAO E SAI DO BATE PAPO \r
{Cor.vermelho}HELP{Cor.reset} \t\t PARA LISTAR OS COMANDOS \r
-----------------------|-----------------------\r\n"""

        return exibeComando

    def broadcast(self, clients, msg):

        for sock in clients:
            if sock != self.conexao.conSocket:
                enviamsg = controlSend(sock)
                enviamsg.send("\r" + str(msg))

    def selfBroadcast(self, msg):
        enviamsg = controlSend(self.conexao.conSocket)
        enviamsg.send("\r" + str(msg))

    def inputCommand(self, inputText):
        splitTexto = inputText.split(" ")
        splitTexto[0] = splitTexto[0].strip()
        print(settings.rooms)
        if splitTexto[0] == 'ENTER':
            # VERIFICA SE JA ESTÁ EM UMA SALA
            if self.salaLogado != "":
                return f"{Cor.ciano}VOCE JA ESTA EM UMA SALA{Cor.reset}, use o comando {Cor.vermelho}EXITROOMS{Cor.reset}\r\n"
            # VERIFICA SE A SALA EXISTE
            for i in range(len(settings.rooms)):

                campoProc = splitTexto[1].replace('\r\n', "").strip()
                if campoProc == settings.rooms[i][0]:
                    self.salaLogado = campoProc
                    self.broadcast(settings.rooms[i][1],
                                   f"{Cor.azul}{self.conexao.infoUser['nameAlias']}{Cor.reset} entrou na sala ;)\r\n")

                    settings.rooms[i][1].append(self.conexao.conSocket)
                    settings.rooms[i][2].append(
                        self.conexao.infoUser['nameAlias'])
                    self.conexao.controlSend.send(
                        f"\rIngressando na sala{Cor.vermelho}...{Cor.reset}")
                    time.sleep(2)
                    self.conexao.controlSend.send(
                        f"\r\n{Cor.verde}Tudo OK !!!{Cor.reset}\r\n")
                    sala = f"| SALA {Cor.verde}{self.salaLogado}{Cor.reset} | {len(settings.rooms[i][2])} online |"
                    return f"""\r
{"-"*(len(sala)-9)}\r
{sala}\r
{"-"*(len(sala)-9)}\r
Bem vindo a sala {Cor.verde}{self.salaLogado}{Cor.reset} ! Digite o comando {Cor.vermelho}CHAT{Cor.reset} para conversar\r
"""
            return "\rSALA INEXISTENTE\r\n"
        elif splitTexto[0] == "CHAT":

            if self.salaLogado == "":
                return "\rEntre em uma sala para enviar msg...\r\n"

            for i in range(len(settings.rooms)):

                if self.salaLogado == settings.rooms[i][0]:
                    self.broadcast(
                        settings.rooms[i][1], f"{Cor.azul}{self.conexao.infoUser['nameAlias']}{Cor.reset} : {str(' '.join(splitTexto[1:]))}")
                    return ""

        elif splitTexto[0] == "ONLINE":
            if self.salaLogado == "":
                return "\rEntre em uma sala para verificar usuarios online...\r\n"

            users = "Usuarios online:\r\n{Cor.amarelo}->{Cor.reset} "

            for i in range(len(settings.rooms)):
                if settings.rooms[i][0] == self.salaLogado:
                    print(settings.rooms[i][2])
                    users += '\r\n{Cor.amarelo}->{Cor.reset} '.join(
                        settings.rooms[i][2])
            users += "\r\n"
            return users

        elif splitTexto[0] == "ROOMS":
            salas = f"Salas disponiveis: Digite o comando {Cor.vermelho}ENTER{Cor.reset} para entrar na sala\r\n"

            for i in range(len(settings.rooms)):
                salas += f"{Cor.amarelo}->{Cor.reset} {Cor.verde}{settings.rooms[i][0]}{Cor.reset}\r\n"

            return salas

        elif splitTexto[0] == "CREATEROOMS":
            # VERIFICA SE JA ESTÁ EM UMA SALA
            if self.salaLogado != "":
                return f"{Cor.ciano}VOCE JA ESTA EM UMA SALA{Cor.reset}, use o comando {Cor.vermelho}EXITROOMS{Cor.reset}\r\n"

            sala = splitTexto[1].replace('\r\n', "").strip()

            if sala == "":
                return "\rInforme o nome de uma sala\r\n"

            settings.rooms.append([sala, [], []])
            return f"Sala {Cor.verde}{sala}{Cor.reset} criada com sucesso!\r\n"

        elif splitTexto[0] == "EXITROOMS":
            sala = splitTexto[1].strip()
            if self.salaLogado != sala:
                return f"Voce nao esta na sala {Cor.verde}{sala}{Cor.reset}!\r\n"
            for i in range(len(settings.rooms)):
                if settings.rooms[i][0] == self.salaLogado:
                    self.salaLogado = ""
                    settings.rooms[i][1].remove(self.conexao.conSocket)
                    settings.rooms[i][2].remove(
                        self.conexao.infoUser['nameAlias'])
                    return 'Voltando a sala principal...\r\n'

        elif splitTexto[0] == "QUIT":
            if not (self.salaLogado):
                self.selfBroadcast(
                    f"Ate a proxima {Cor.azul + self.conexao.infoUser['nameAlias'].upper() + Cor.reset}!\r")
                time.sleep(2)
                self.conexao.conSocket.close()
                return ""
            for i in range(len(settings.rooms)):
                if settings.rooms[i][0] == self.salaLogado:
                    self.salaLogado = ""
                    settings.rooms[i][1].remove(self.conexao.conSocket)
                    settings.rooms[i][2].remove(
                        self.conexao.infoUser['nameAlias'])
                    self.selfBroadcast(
                        f"Ate a proxima {Cor.azul + self.conexao.infoUser['nameAlias'].upper() + Cor.reset}!\r\n")
                    self.broadcast(
                        settings.rooms[i][1], f"{Cor.azul +self.conexao.infoUser['nameAlias'] + Cor.reset} saiu da sala ;(\r\n")
                    time.sleep(2)
                    self.conexao.conSocket.close()
                    return ""

        elif splitTexto[0] == "HELP":
            print('to aqui')
            help = self.commands()
            return help

        else:
            return "\rCOMANDO NAO DISPONIVEL\r\n"
