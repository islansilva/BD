import os
import sys
import time
import json
from controlSend import controlSend
from funcoes.colors import Cor
from funcoes.BatePapo import BatePapo

sys.path.append(os.path.abspath("../BatePapo"))


class Login():

    def __init__(self, conSocket):
        self.conSocket = conSocket
        self.controlSend = controlSend(conSocket)
        self.infoUser = {'login': '', 'pass': '', 'nameAlias': ''}
        self.isLogged = 0
        self.login = ""
        self.nickname = ""
        self.password = ""
        self.controlSend.send("\u001B[2J")
        self.controlSend.send("\033[H")
        self.controlSend.send(
            f"Seja bem vindo (a) a mais badalada sala de bate papo do Brasil.\r\nCOMANDOS:\r\n")
        self.controlSend.send(self.commands())
        while not self.isLogged:
            # VERIFICA O VALOR INSERIDO NO COMANDO LOGIN
            self.userLogin()

            checkUser, dataJson = self.userExist(self.infoUser)
            # Caso o usuário exista, solicita a senha
            if(checkUser):
                
                # Realiza a comparação
                if dataJson['pass'].strip() == self.infoUser['pass'].strip():
                    self.infoUser['nameAlias'] = dataJson['nameAlias'].strip()
                    self.controlSend.send(f"\r\n{Cor.ciano}LOGADO!{Cor.reset}")
                    self.isLogged = 1
                else:
                    self.infoUser = self.infoUser.fromkeys(self.infoUser,"")
                    self.login = self.password = ""
                    self.controlSend.send(f"{Cor.ciano}SENHA INCORRETA{Cor.reset} -> DIGITE NOVAMENTE O COMANDO LOGIN\r\n")

            else:          
                self.controlSend.send("LOGIN NAO EXISTE!!\r\n")

                self.controlSend.send(
                    f'{Cor.amarelo}Criar CONTA{Cor.reset} (login sera o inserido no ultima comando)\r\n')
                while not self.infoUser['nameAlias']:
                    # Digitar o nome do usuario para cadstro
                    self.controlSend.send("\rNickname: ")
                    while self.nickname[-1:] != "\n":
                        self.nickname += str(conSocket.recv(1024).decode('UTF-8'))
                        if(self.nickname[-1:] == "\b"):
                            self.nickname = self.nickname.replace("\b", "")
                            self.nickname = self.nickname[:-1]
                            self.controlSend.send("\u001B[J")
                                
                    self.nickname = self.nickname.split(" ")
                    if self.nickname[0] != 'USER':
                        self.nickname = ""
                        self.controlSend.send("COMANDO NAO DISPONIVEL\r\n")
                    else:
                        self.infoUser['nameAlias'] = self.nickname[1].strip()

                # Digitar a senha para cadastro do usuário
                self.infoUser['pass'] = ""
                while not self.infoUser['pass']:
                    # Digitar o nome do usuario para cadstro
                    self.controlSend.send("\rSenha: ")

                    while self.password[-1:] != "\n":
                        self.password += str(conSocket.recv(1024).decode('UTF-8'))
                        if(self.password[-1:] == "\b"):
                            self.password = self.password.replace("\b", "")
                            self.password = self.password[:-1]
                            self.controlSend.send("\u001B[J")

                    
                    self.password = self.password.split(" ")
                    if self.password[0] != 'PASS':
                        self.password = ""
                        self.controlSend.send("COMANDO NAO DISPONIVEL\r\n")
                    else:
                        self.infoUser['pass'] = self.password[1].strip()   

                
                self.createUser(self.infoUser)
                self.isLogged = 1
                self.controlSend.send(f"\r\nUsuario criado com sucesso!!!")

        time.sleep(2)
        self.loginSucesso()


    def userLogin(self):
        while not self.infoUser['login']:
            self.controlSend.send("\r\nLogin: ")
            while self.login[-1:] != "\n":
                self.login += str(self.conSocket.recv(1024).decode())
                if(self.login[-1:] == "\b"):
                    self.login = str(self.login).replace("\b", "")
                    self.login = self.login[:-1]
                    self.controlSend.send("\u001B[J")

            self.login = self.login.split(" ")
            if self.login[0] != 'LOGIN':
                self.login = ""
                self.controlSend.send("COMANDO NAO DISPONIVEL\r\n")
            else:
                try:
                    self.infoUser['login'] = self.login[1].strip()
                    self.infoUser['pass'] = self.login[2].strip()
                except:
                    continue


    def userExist(self, dataLogin, filename="db/user.json"):
        with open(filename) as json_file:
            data = json.load(json_file)
            for i in range(len(data['users'])):

                if str(data['users'][i]['login']) == dataLogin['login'].replace("\n", ""):
                    json_file.close()
                    return True, data['users'][i]

            json_file.close()
            return False, ""

    def createUser(self, dataLogin, filename="db/user.json"):

        with open(filename) as json_file:
            data = json.load(json_file)

            data['users'].append(dataLogin)
        json_file.close()

        with open(filename, 'w') as f:
            
            json.dump(data, f, indent=4)

        f.close()
    
    def commands(self):
        exibeComando = f"""-----------------------|-----------------------\r
{Cor.vermelho}LOGIN{Cor.reset} \t FAZER LOGIN (formato -> LOGIN login senha) \r
{Cor.vermelho}USER{Cor.reset} \t INSERIR NOVO NICKNAME AO NOVO USUARIO\r
{Cor.vermelho}PASS{Cor.reset} \t INSERIR NOVA SENHA AO NOVO USUARIO\r
{Cor.amarelo}Usuarios ja cadastrados:{Cor.reset}\r
{Cor.vermelho}EXEMPLO 1{Cor.reset}  LOGIN Islan 1234ab\r
{Cor.vermelho}EXEMPLO 2{Cor.reset}  LOGIN alee bizz\r
-----------------------|-----------------------\r\n"""
        return exibeComando

    def loginSucesso(self):

        batePapo = BatePapo(self)
        self.controlSend.send("\u001B[2J")
        self.controlSend.send("\033[H")
        bemVindo = f"\rBem Vindo, {Cor.azul + str(self.infoUser['nameAlias']).upper() + Cor.reset}\r\n"
        self.controlSend.send(bemVindo)
        help = batePapo.commands()
        self.controlSend.send(help)
        

        while True:

            inputCom = ""
            try:
                while  inputCom[-1:] != "\n":
                    inputCom = inputCom + str(self.conSocket.recv(1024).decode('latin-1'))

                    if(inputCom[-1:] == "\b"):
                        inputCom = str(inputCom).replace("\b", "")
                        inputCom = inputCom[:-1]
                        self.controlSend.send("\u001B[J")
                clientMessage = batePapo.inputCommand(inputCom)
                
                self.controlSend.send(clientMessage)
            except:
                break

