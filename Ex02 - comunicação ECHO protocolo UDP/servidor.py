'''
DISCENTES: Evelen Pinheiro de Oliveira e Marcos Eduardo da Silva Braga
EXERCÍCIO 02 - COMUNICAÇÃO ECHO COM PROTOCOLO UDP

'''
import socket

# Dados de endereçamento do socket do servior
HOST = "localhost"
PORT = 6000
# Tamanho máximo da mensagem recebida 64kb
TAMANHO_BUFFER = 64000 

# Criação do socket do servidor
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket UDP criado com sucesso!")

# Vinculando o endereço ao socket do servidor
socket_servidor.bind((HOST, PORT))
print(f"Servidor UDP vinculado a {HOST}:{PORT}")

while True:
    try:
        dado, endereco = socket_servidor.recvfrom(TAMANHO_BUFFER) # Recebendo dados
        mensagem = dado.decode('utf-8')
        print(f"Mensagem recebida de {endereco}: {mensagem}")
        socket_servidor.sendto(dado, endereco) # Enviando ECHO
    
    except socket.error as err:
        print(f"Ocorreu um erro de socket: {err}")

    except KeyboardInterrupt:
        print('Servidor desligado.')