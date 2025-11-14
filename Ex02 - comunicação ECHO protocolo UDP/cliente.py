'''
DISCENTES: Evelen Pinheiro de Oliveira e Marcos Eduardo da Silva Braga
EXERCÍCIO 02 - COMUNICAÇÃO ECHO COM PROTOCOLO UDP

'''
import socket

# Dados do endereço do servidor
HOST_SERVIDOR = "localhost"
PORT_SERVIDOR = 6000
# Tamanho máximo do buffer da mensagem 64kb
TAMANHO_BUFFER = 64000 

# Criação do socket do cliente
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente.settimeout(10) # Limite de tempo de resposta do servidor
print("Socket UDP criado com sucesso!")

try:
    while True:
        mensagem = str(input("Digite sua mensagem ou 'sair': "))
        mensagem_code = mensagem.encode('utf-8')

        if mensagem.lower().strip() == 'sair':
            print("Cliente encerrado.")
            socket_cliente.close()
            break
        # Validação do tamnho da mensagem
        if len(mensagem_code) > TAMANHO_BUFFER: 
            print(f"Erro: Sua mensagem é muita longa ({len(mensagem_code)} bytes)")
            print(f"O tamanho total do buffer é de {TAMANHO_BUFFER} bytes")
            continue
        else:
            socket_cliente.sendto(mensagem_code,(HOST_SERVIDOR, PORT_SERVIDOR)) # Enviando mensagem ao servidor
            dado, endereco = socket_cliente.recvfrom(TAMANHO_BUFFER) # Recebendo o ECHO
            echo = dado.decode('utf-8')
            print(f"ECHO: {echo}")

# Tratamento do erro de timeout
except socket.timeout:
    print("A operação excedeu o tempo limite!")
    socket_cliente.close()

# Tratamento de outros erros - o UDP não tem um tratamento específico para perdas de pacote
except socket.error as err:
    print(f"Ocorreu um erro de socket: {err}")
    socket_cliente.close()