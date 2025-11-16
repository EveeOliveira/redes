'''
DISCENTES: Evelen Pinheiro de Oliveira e Marcos Eduardo da Silva Braga
EXERCÍCIO 01 - COMUNICAÇÃO CLIENTE-SERVIDOR COM PROTOCOLO TCP

'''
import socket

HOST = '127.0.0.1'    # Endereço de IP que fará a conexão (localhost)
PORT = 5000           # Porta em que fará a conexão

# Cria um socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))       # Conecta ao servidor especificado pelo HOST e PORT

    mensagem = 'Olá Servidor!'
    s.sendall(mensagem.encode())  # Envia a mensagem após codificá-la para bytes

    data = s.recv(1024)           # Aguarda a resposta do servidor (até 1024 bytes)
    print(f'Resposta do servidor: {data.decode()}')

    s.close()                     # Fecha o socket