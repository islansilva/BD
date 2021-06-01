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
{Cor.vermelho}EXITROOM{Cor.reset} \t SAIR DA SALA \r
{Cor.vermelho}QUIT{Cor.reset} \t\t ENCERRA A CONEXAO E SAI DO BATE PAPO \r
{Cor.vermelho}HELP{Cor.reset} \t\t PARA LISTAR OS COMANDOS \r
-----------------------|-----------------------\r\n"""

        return exibeComando

    def broadcast(self, clients, msg):

        for sock in clients:
            if sock != self.conexao.conSocket:
                try:
                    enviamsg = controlSend(sock)
                    enviamsg.send("\r" + str(msg))
                except ConnectionAbortedError:
                    for i in range(len(settings.rooms)):
                        if settings.rooms[i][0] == self.salaLogado:
                            for j in range (len(settings.rooms[i][1])):
                                if settings.rooms[i][1][j] == sock:
                                    nick = settings.rooms[i][2][j]
                                    settings.rooms[i][1].remove(sock)
                                    settings.rooms[i][2].remove(nick)
                                    break
                            break

    def selfBroadcast(self, msg):
        enviamsg = controlSend(self.conexao.conSocket)
        enviamsg.send("\r" + str(msg))

    def inputCommand(self, inputText):
        splitTexto = inputText.split(" ")
        splitTexto[0] = splitTexto[0].strip()

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
                    time.sleep(1)
                    self.conexao.controlSend.send("\u001B[2J")
                    self.conexao.controlSend.send("\033[H")
                    sala = f"| SALA {Cor.verde}{self.salaLogado}{Cor.reset} | {len(settings.rooms[i][2])} online |"
                    return f"""\r{"-"*(len(sala)-9)}\r
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
                    return f"{Cor.magenta}Eu{Cor.reset}: {str(' '.join(splitTexto[1:]))}"

        elif splitTexto[0] == "ONLINE":
            if self.salaLogado == "":
                return "\rEntre em uma sala para verificar usuarios online...\r\n"

            users = f"Usuarios online:\r\n{Cor.amarelo}->{Cor.reset} "

            for i in range(len(settings.rooms)):
                if settings.rooms[i][0] == self.salaLogado:
                    users += f'\r\n{Cor.amarelo}->{Cor.reset} '.join(
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
                return f"{Cor.ciano}VOCE JA ESTA EM UMA SALA{Cor.reset}, use o comando {Cor.vermelho}EXITROOM{Cor.reset}\r\n"

            try:
                sala = splitTexto[1].strip()
            except:
                return "\rInforme o nome de uma sala\r\n"

            if sala == "":
                return "\rInforme o nome de uma sala\r\n"
            else:
                settings.rooms.append([sala, [], []])
                return f"Sala {Cor.verde}{sala}{Cor.reset} criada com sucesso!\r\n"

        elif splitTexto[0] == "EXITROOM":
            if self.salaLogado == "":
                return f"Voce nao esta em nenhuma sala!\r\n"
            for i in range(len(settings.rooms)):
                if settings.rooms[i][0] == self.salaLogado:
                    self.salaLogado = ""
                    settings.rooms[i][1].remove(self.conexao.conSocket)
                    settings.rooms[i][2].remove(
                        self.conexao.infoUser['nameAlias'])
                    self.broadcast(
                        settings.rooms[i][1], f"{Cor.azul +self.conexao.infoUser['nameAlias'] + Cor.reset} saiu da sala ;(\r\n")
                    self.conexao.controlSend.send(f'Voltando a sala principal{Cor.vermelho}...{Cor.reset}\r\n')
                    time.sleep(2)
                    self.conexao.controlSend.send(
                        f"{Cor.verde}Tudo OK !!!{Cor.reset}\r\n")
                    time.sleep(1)
                    self.conexao.controlSend.send("\u001B[2J")
                    self.conexao.controlSend.send("\033[H")
                    return self.commands()

        elif splitTexto[0] == "QUIT":
            cliente = {'sala': self.salaLogado, 'sock': str(self.conexao.conSocket), 'nick': self.conexao.infoUser['nameAlias']}
            if not (self.salaLogado):
                self.selfBroadcast(
                    f"Ate a proxima {Cor.azul + self.conexao.infoUser['nameAlias'].upper() + Cor.reset}!")
                time.sleep(2)
                self.conexao.conSocket.close()
                return cliente
            for i in range(len(settings.rooms)):
                if settings.rooms[i][0] == self.salaLogado:
                    self.salaLogado = ""
                    settings.rooms[i][1].remove(self.conexao.conSocket)
                    settings.rooms[i][2].remove(
                        self.conexao.infoUser['nameAlias'])
                    self.selfBroadcast(
                        f"Ate a proxima {Cor.azul + self.conexao.infoUser['nameAlias'].upper() + Cor.reset}!")
                    self.broadcast(
                        settings.rooms[i][1], f"{Cor.azul +self.conexao.infoUser['nameAlias'] + Cor.reset} saiu da sala ;(\r\n")
                    time.sleep(2)
                    self.conexao.conSocket.close()
                    return cliente

        elif splitTexto[0] == "HELP":

            help = self.commands()
            return help

        else:
            return "\rCOMANDO NAO DISPONIVEL\r\n"
