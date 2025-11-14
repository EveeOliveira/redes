'''
DISCENTES: Evelen Pinheiro de Oliveira e Marcos Eduardo da Silva Braga
EXERCÍCIO 04 - Servidor de horas com protocolo TCP

'''

import socket
from datetime import datetime
import threading

# Função que retorna a hora atual já codificada
def horaAtual():
    return datetime.now().strftime("%H:%M:%S").encode('utf-8')

# Fução para cuidar de cada cliente
def handleCliente(socket_cliente, endereco):
    print(f"Solicitação recebida do cliente : {endereco}!")
    # Tratamento de erro por cliente
    try:
        socket_cliente.send(horaAtual())
    except Exception as e:
        print(f"ERRO: Erro ao comunicar com o cliente {endereco}")
    finally:
        print("Solicitação atendida!")
        socket_cliente.close()
    
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
print("Esperando conexões ...")

while True:
    # Aceitando conexões
    socket_cliente, endereco = socket_servidor.accept()
    
    # Abrindo uma nova thread para cada cliente aceito
    thread_cliente = threading.Thread(
        target=handleCliente,
        args=(socket_cliente, endereco)
    )
    thread_cliente.start()