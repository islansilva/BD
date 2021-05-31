class BatePapo:
    

    def __init__(self, userData):
        pass


    @staticmethod
    def createRoom():

        #0 =  Nome
        #1 =  Sockets
        arrRoom = [['Futebol', [], []], ['Namoro', [], []], ['Carros', [], []]]


        return arrRoom

    def commands(self):
        exibeComando = """\r
INSERT \t\t ENVIAR MENSAGEM \r
ONLINE \t\t VERIFICAR USUARIOS ONLINE \r
ROOMS \t\t SALAS EXISTENTES \r
CREATEROOMS \t CRIAR NOVAS SALAS DE BATE PAPO \r
ENTERROOMS \t ENTRAR EM UMA SALA \r
EXITROOMS \t SAIR DA SALA \r
QUIT \t\t ENCERRA A CONEXAO E SAI DO BATE PAPO \r
HELP \t\t PARA LISTAR OS COMANDOS \r""" 

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

        #dispCommands = ['INSERT', 'ONLINE', 'ROOMS', 'CREATEROOMS', 'ENTERROOMS', 'EXITROOMS', 'QUIT', 'HELP']

        print(settings.rooms)
        splitTexto = inputText.split(" ")

        if splitTexto[0] == 'ENTER':
            #VERIFICA SE A SALA EXISTE
            for i in range(len(settings.rooms)):
                
                campoProc = splitTexto[1].replace('\r\n', "").strip()
                if campoProc == settings.rooms[i][0]:
                    self.salaLogado = campoProc;
                    self.broadcast(settings.rooms[i][1], str(self.conexao.infoUser['nameAlias']) + " entrou na sala")

                    settings.rooms[i][1].append(self.conexao.conSocket)
                    settings.rooms[i][2].append(self.conexao.infoUser['nameAlias'])
                    
                    return "\rIngressando na sala...\r\n"
            print(settings.rooms)
            return "\rSALA INEXISTENTE\r\n"
        elif splitTexto[0] == "CHAT":

            if self.salaLogado == "":
                return "\rEntre em uma sala para enviar msg...\r\n"


            for i in range(len(settings.rooms)):

                if self.salaLogado == settings.rooms[i][0]:
                    self.broadcast(settings.rooms[i][1],self.conexao.infoUser['nameAlias'] + ": " + str(" ".join(splitTexto[1:])))
                    return ""
        
        elif splitTexto[0] == "ONLINE":
            if self.salaLogado == "":
                return "\rEntre em uma sala para verificar usuários online...\r\n"


            for i in range(len(settings.rooms)):
                for x in settings.rooms[i][2]:
                    self.broadcast(str(settings.rooms[i][2][x]) + " esta online")

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
