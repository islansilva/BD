# 💻 PYTHON CHAT SERVER

Projeto desenvolvido na matéria de Tópicos Avançados de Redes de Computadores com o intuito de implementar um chat no terminal em python com o client-server protocol Telnet.
Aceita múltiplos cliente inseridos via terminal.

### Integrantes

* ISLAN SILVA FIGUEREDO       &emsp;&emsp;&emsp;&emsp;&emsp;                          RA: 22.119.027-5 <br />
* LUCAS DA SILVA OLIVEIRA     &emsp;&emsp;&emsp;&emsp;&nbsp;                          RA: 22.119.031-7 <br />
* ALESSANDRO BIZ              &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;        RA: 22.119.038-2 <br />
* IVAN SANCHEZ TUZITA         &emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;        RA: 22.119.040-8 <br />

## 🚀 Início
Primeira coisa ao baixar o arquivo é iniciar do diretório Projeto1 o arquivo <b>main.py</b>

```bash

# Clone o repositório
git clone https://github.com/islansilva/BD.git

# Acesse o projeto
cd BD

# Run
python main.py

#ou
python3 main.py
```

## :book: COMANDOS
Todos os comandos devem ser inseridos com letra maiúsculas, caso seja inserido com minúscula o programa recusará

* LOGIN<br />
O comando LOGIN é usado para realizar o login. Recebe os parâmetros login e senha, caso o login exista e a senha esteja correta o usuário é redirecionado ao bate-papo:

![login](https://github.com/islansilva/BD/blob/master/images/login.png) 

* USER<br />
O comando USER é usado para criar um nickname. Recebe o parâmetro nickname, pode ser inserido caso o login não exista e o usuário deseja criar um novo:

![user](https://github.com/islansilva/BD/blob/master/images/user.png) 

* PASS<br />
O comando PASS é usado para criar uma senha. Recebe o parâmetro senha, pode ser inserido caso o login não exista e o usuário deseja criar um novo:

![pass](https://github.com/islansilva/BD/blob/master/images/pass.png) 

* ENTER<br />
O comando ENTER é usado para entrar em uma sala. Recebe o parâmetro sala, caso ela exista, o usuário acessa:

![enter](https://github.com/islansilva/BD/blob/master/images/enter.png) 

* CHAT<br />
O comando CHAT é usado para conversar em uma sala. Recebe qualquer quantidade de parâmetros para ser a frase, o usuário <b>deve</b> estar em uma sala:

![chat](https://github.com/islansilva/BD/blob/master/images/chat.png) 

* ONLINE<br />
O comando USER é usado para visualizar quem está online na sala. Não recebe parâmetro, o usuário <b>deve</b> estar em uma sala:

![online](https://github.com/islansilva/BD/blob/master/images/online.png) 

* ROOMS<br />
O comando ROOMS é usado para verificar as salas disponíveis. Não recebe parâmetro, o usuário pode inserir o comando estando ou não em uma sala:

![rooms](https://github.com/islansilva/BD/blob/master/images/rooms.png) 

* CREATEROOMS<br />
O comando CREATEROOMS é usado para criar uma nova sala. Recebe o parâmetro nome da sala (só uma palavra), o usuário <b>deve</b> estar no menu principal do bate-papo:

![createrooms](https://github.com/islansilva/BD/blob/master/images/createrooms.png) 

* EXITROOM<br />
O comando EXITROOM é usado para sair de uma sala. Não recebe parâmetro, o usuário <b>deve</b> estar em uma sala:

![exitroom](https://github.com/islansilva/BD/blob/master/images/exitroom.png) 

* QUIT<br />
O comando QUIT é usado para encerrar o usuário. Não recebe parâmetro, o usuário pode inserir o comando estando ou não em uma sala:

![quit](https://github.com/islansilva/BD/blob/master/images/quit.png) 

* HELP<br />
O comando HELP é usado para exibir a lista de comandos. Não recebe parâmetro, o usuário pode inserir o comando estando ou não em uma sala:

![help](https://github.com/islansilva/BD/blob/master/images/help.png) 
