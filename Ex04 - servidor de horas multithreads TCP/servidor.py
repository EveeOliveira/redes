'''
DISCENTES: Evelen Pinheiro de Oliveira e Marcos Eduardo da Silva Braga
EXERCÍCIO 04 - Servidor de horas com protocolo TCP

'''

import socket
from datetime import datetime

def horaAtual():
    return datetime.now().strftime("%H:%M:%S")

# Dados do endereço do servidor
HOST = "localhost"
PORT = 7000

# Criação do socket do servidor
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket TCP criado com sucesso!")

# Vinculando o endereço ao socket
socket_servidor.bind((HOST, PORT))

# Criando canal de escuta do servidor
socket_servidor.listen(8) # Número de conexões pendentes = 8
print('Esperando conexões ...')

while True:
    # Aceitando conexões
    socket_cliente, endereco = socket_servidor.accept()
    horas = horaAtual().encode('utf-8')
    socket_cliente.send(horas)