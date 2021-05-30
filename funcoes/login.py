import json
import sys
import os

sys.path.append(os.path.abspath("../BatePapo"))
from controlSend import controlSend




class Login():

    def __init__(self, conSocket):
        self.conSocket = conSocket
        self.controlSend = controlSend(conSocket)
        infoUser = {'login': '', 'pass': '', 'nameAlias': ''}

        self.controlSend.send("Seja bem vindo (a) a mais badalada sala de bate papo do Brasil. \r\nPor favor, digite seu usuario e senha \r\n\r\nLogin: ")

        while  infoUser['login'][-1:] != "\n":
            infoUser['login'] = str(infoUser['login']) + str(conSocket.recv(1024).decode('UTF-8'))
            if(infoUser['login'][-1:] == "\b"):
                  infoUser['login'] = str(infoUser['login']).replace("\b", "")
     
        infoUser['login'] = infoUser['login'].replace("\r\n", "")

        checkUser, dataJson = self.userExist(infoUser)

        #Caso o usuário exista, solicita a senha
        if(checkUser):

            #Solicita a senha
            while infoUser['pass'].replace("\n", "").strip() == "":
                infoUser['pass'] = ""
                self.controlSend.send("\r\nDigite uma senha: ")

                while  infoUser['pass'][-1:] != "\n":
                    infoUser['pass'] = str(infoUser['pass']) + str(conSocket.recv(1024).decode('UTF-8')).replace("\b", "") 

                #Realiza a comparação
                if dataJson['pass'].strip() == infoUser['pass'].strip():
                    self.loginSucesso()
                else:
                    infoUser['pass'] = ""
                    self.controlSend.send("Senha incorreta\r\n")

        else:
            self.controlSend.send("LOGIN NAO EXISTE!!\r\n")
            
            #Digitar o nome do usuario para cadstro
            while infoUser['nameAlias'].replace("\n", "").strip() == "":
                infoUser['nameAlias'] = ""
                self.controlSend.send("Criar Login: \r\nNome de usuario: ")

                while  infoUser['nameAlias'][-1:] != "\n":
                    infoUser['nameAlias'] = str(infoUser['nameAlias']) + str(conSocket.recv(1024).decode('UTF-8')).replace("\b", "") 
                print(infoUser['nameAlias'])
            #Digitar a senha para cadastro do usuário
            while infoUser['pass'].replace("\n", "").strip() == "":
                infoUser['pass'] = ""
                self.controlSend.send("\r\nDigite uma senha: ")

                while  infoUser['pass'][-1:] != "\n":
                    infoUser['pass'] = str(infoUser['pass']) + str(conSocket.recv(1024).decode('UTF-8')).replace("\b", "") 
                print(infoUser['nameAlias'])

                infoUser['nameAlias'] = infoUser['nameAlias'].replace("\r\n","")
                infoUser['pass'] =  infoUser['pass'].replace("\r\n","") 
                infoUser['login'] = infoUser['login'].replace("\r\n","") 

            self.createUser(infoUser)
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
        self.controlSend.send("\u001B[2J")
        self.controlSend.send("opa bom dia")
