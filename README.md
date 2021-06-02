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

<img src = "https://github.com/islansilva/BD/blob/master/images/login.png" width = 500 height = 250 />

* USER<br />
O comando USER é usado para criar um nickname. Recebe o parâmetro nickname, pode ser inserido caso o login não exista e o usuário deseja criar um novo:

<img src = "https://github.com/islansilva/BD/blob/master/images/user.png" width = 510 height = 280 />

* PASS<br />
O comando PASS é usado para criar uma senha. Recebe o parâmetro senha, pode ser inserido caso o login não exista e o usuário deseja criar um novo:

<img src = "https://github.com/islansilva/BD/blob/master/images/pass.png" width = 510 height = 320 />

* ENTER<br />
O comando ENTER é usado para entrar em uma sala. Recebe o parâmetro sala, caso ela exista, o usuário acessa:

<img src = "https://github.com/islansilva/BD/blob/master/images/enter.png" width = 550 height = 250 />

* CHAT<br />
O comando CHAT é usado para conversar em uma sala. Recebe qualquer quantidade de parâmetros para ser a frase, o usuário <b>deve</b> estar em uma sala:

<img src = "https://github.com/islansilva/BD/blob/master/images/chat.png" width = 500 height = 210 />

* ONLINE<br />
O comando USER é usado para visualizar quem está online na sala. Não recebe parâmetro, o usuário <b>deve</b> estar em uma sala:

<img src = "https://github.com/islansilva/BD/blob/master/images/online.png" width = 500 height = 230 />

* ROOMS<br />
O comando ROOMS é usado para verificar as salas disponíveis. Não recebe parâmetro, o usuário pode inserir o comando estando ou não em uma sala:

<img src = "https://github.com/islansilva/BD/blob/master/images/rooms.png" width = 500 height = 330 />

* CREATEROOMS<br />
O comando CREATEROOMS é usado para criar uma nova sala. Recebe o parâmetro nome da sala (só uma palavra), o usuário <b>deve</b> estar no menu principal do bate-papo:

<img src = "https://github.com/islansilva/BD/blob/master/images/createrooms.png" width = 430 height = 230 />

* EXITROOM<br />
O comando EXITROOM é usado para sair de uma sala. Não recebe parâmetro, o usuário <b>deve</b> estar em uma sala:

<img src = "https://github.com/islansilva/BD/blob/master/images/exitroom.png" width = 500 height = 290 />

* QUIT<br />
O comando QUIT é usado para encerrar o usuário. Não recebe parâmetro, o usuário pode inserir o comando estando ou não em uma sala:

<img src = "https://github.com/islansilva/BD/blob/master/images/quit.png" width = 450 height = 270 />

* HELP<br />
O comando HELP é usado para exibir a lista de comandos. Não recebe parâmetro, o usuário pode inserir o comando estando ou não em uma sala:

<img src = "https://github.com/islansilva/BD/blob/master/images/help.png" width = 500 height = 300 />
