class BatePapo:
    

    def __init__(self, userData):
        pass

    @staticmethod
    def createRoom():

        #0 =  Nome
        #1 =  Sockets
        arrRoom = [['Futebol', []], ['Namoro', []], ['Carros', []]]

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

        return exibeComando

        
    def inputCommand(self, inputText):

        dispCommands = ['INSERT', 'ONLINE', 'ROOMS', 'CREATEROOMS', 'ENTERROOMS', 'EXITROOMS', 'QUIT', 'HELP']


        splitTexto = inputText.split(" ")

        if not splitTexto[0] in dispCommands:
            ret = "COMANDO NÃO DISPONÍVEL"
