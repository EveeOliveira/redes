'''
DISCENTES: Evelen Pinheiro de Oliveira e Marcos Eduardo da Silva Braga
EXERCÍCIO 04 - Servidor de horas com protocolo TCP

'''
import socket

# Dados do endereço do servidor
HOST_SERVIDOR = "localhost"
PORT_SERVIDOR = 7000

# Criando socket TCP do cliente
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket TCP criado com sucesso!")

# Criando a conexão com o servidor
socket_cliente.connect((HOST_SERVIDOR, PORT_SERVIDOR))

# Recebendo horas
horas = socket_cliente.recv(1024)
print(f"Mensagem do Servidor: {horas.decode('utf-8')}")