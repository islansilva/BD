from controlSend import controlSend
import json
import sys
import os


from funcoes.BatePapo import BatePapo

sys.path.append(os.path.abspath("../BatePapo"))


class Login():

    def __init__(self, conSocket):
        self.conSocket = conSocket
        self.controlSend = controlSend(conSocket)
        self.infoUser = {'login': '', 'pass': '', 'nameAlias': ''}

        self.controlSend.send(
            "Seja bem vindo (a) a mais badalada sala de bate papo do Brasil. \r\nPor favor, digite seu usuario e senha \r\n\r\nLogin: ")

<<<<<<< Updated upstream
        while  self.infoUser['login'][-1:] != "\n":
            self.infoUser['login'] = str(self.infoUser['login']) + str(conSocket.recv(1024).decode('UTF-8'))
            if(self.infoUser['login'][-1:] == "\b"):
                  self.infoUser['login'] = str(self.infoUser['login']).replace("\b", "")
                  self.controlSend.send("\u001b[0x08")
     
        self.infoUser['login'] = self.infoUser['login'].replace("\r\n", "")
=======
        while infoUser['login'][-1:] != "\n":
            infoUser['login'] = str(infoUser['login']) + \
                str(conSocket.recv(1024).decode('UTF-8'))
            if(infoUser['login'][-1:] == "\b"):
                infoUser['login'] = str(infoUser['login']).replace("\b", "")

        infoUser['login'] = infoUser['login'].replace("\r\n", "")
>>>>>>> Stashed changes

        checkUser, dataJson = self.userExist(self.infoUser)

        # Caso o usuário exista, solicita a senha
        if(checkUser):

<<<<<<< Updated upstream
            #Solicita a senha
            while self.infoUser['pass'].replace("\n", "").strip() == "":
                self.infoUser['pass'] = ""
                self.controlSend.send("\r\nDigite uma senha: ")

                while  self.infoUser['pass'][-1:] != "\n":
                    self.infoUser['pass'] = str(self.infoUser['pass']) + str(conSocket.recv(1024).decode('UTF-8')).replace("\b", "") 

                #Realiza a comparação
                if dataJson['pass'].strip() == self.infoUser['pass'].strip():
                    self.infoUser['nameAlias'] = dataJson['nameAlias'].strip();
=======
            # Solicita a senha
            while infoUser['pass'].replace("\n", "").strip() == "":
                infoUser['pass'] = ""
                self.controlSend.send("\r\nDigite uma senha: ")

                while infoUser['pass'][-1:] != "\n":
                    infoUser['pass'] = str(
                        infoUser['pass']) + str(conSocket.recv(1024).decode('UTF-8')).replace("\b", "")

                # Realiza a comparação
                if dataJson['pass'].strip() == infoUser['pass'].strip():
>>>>>>> Stashed changes
                    self.loginSucesso()
                else:
                    self.infoUser['pass'] = ""
                    self.controlSend.send("Senha incorreta\r\n")

        else:
            self.controlSend.send("LOGIN NAO EXISTE!!\r\n")
<<<<<<< Updated upstream
            
            #Digitar o nome do usuario para cadstro
            while self.infoUser['nameAlias'].replace("\n", "").strip() == "":
                self.infoUser['nameAlias'] = ""
                self.controlSend.send("Criar Login: \r\nNome de usuario: ")

                while  self.infoUser['nameAlias'][-1:] != "\n":
                    self.infoUser['nameAlias'] = str(self.infoUser['nameAlias']) + str(conSocket.recv(1024).decode('UTF-8')).replace("\b", "") 
                print(self.infoUser['nameAlias'])
            #Digitar a senha para cadastro do usuário
            while self.infoUser['pass'].replace("\n", "").strip() == "":
                self.infoUser['pass'] = ""
                self.controlSend.send("\r\nDigite uma senha: ")

                while  self.infoUser['pass'][-1:] != "\n":
                    self.infoUser['pass'] = str(self.infoUser['pass']) + str(conSocket.recv(1024).decode('UTF-8')).replace("\b", "") 
                print(self.infoUser['nameAlias'])

                self.infoUser['nameAlias'] = self.infoUser['nameAlias'].replace("\r\n","")
                self.infoUser['pass'] =  self.infoUser['pass'].replace("\r\n","") 
                self.infoUser['login'] = self.infoUser['login'].replace("\r\n","") 
=======

            # Digitar o nome do usuario para cadstro
            while infoUser['nameAlias'].replace("\n", "").strip() == "":
                infoUser['nameAlias'] = ""
                self.controlSend.send("Criar Login: \r\nNome de usuario: ")

                while infoUser['nameAlias'][-1:] != "\n":
                    infoUser['nameAlias'] = str(
                        infoUser['nameAlias']) + str(conSocket.recv(1024).decode('UTF-8')).replace("\b", "")
                print(infoUser['nameAlias'])
            # Digitar a senha para cadastro do usuário
            while infoUser['pass'].replace("\n", "").strip() == "":
                infoUser['pass'] = ""
                self.controlSend.send("\r\nDigite uma senha: ")

                while infoUser['pass'][-1:] != "\n":
                    infoUser['pass'] = str(
                        infoUser['pass']) + str(conSocket.recv(1024).decode('UTF-8')).replace("\b", "")
                print(infoUser['nameAlias'])

                infoUser['nameAlias'] = infoUser['nameAlias'].replace(
                    "\r\n", "")
                infoUser['pass'] = infoUser['pass'].replace("\r\n", "")
                infoUser['login'] = infoUser['login'].replace("\r\n", "")
>>>>>>> Stashed changes

            self.createUser(self.infoUser)
            self.controlSend.send("\r\nUsuario criado com sucesso!!!")
            self.loginSucesso()

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
            print("4")
            json.dump(data, f, indent=4)

        f.close()

    def loginSucesso(self):

        batePapo = BatePapo(self)
        self.controlSend.send("\u001B[2J")
        print(self)
        print(self.infoUser)
        bemVindo = "BEEEEM VINDO " + str(self.infoUser['nameAlias']).upper() + "\n"
        self.controlSend.send(bemVindo)
        help = batePapo.commands()
        self.controlSend.send(help)

        while True:
            inputCom = batePapo.inputCommand(str(self.conSocket.recv(1024).decode('UTF-8')))
            self.controlSend.send(inputCom)
