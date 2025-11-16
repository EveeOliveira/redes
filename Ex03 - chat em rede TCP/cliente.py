'''
DISCENTES: Evelen Pinheiro de Oliveira e Marcos Eduardo da Silva Braga
EXERCÍCIO 03 - CHAT EM REDE COM PROTOCOLO TCP

'''
import socket, threading

HOST = '127.0.0.1'
PORT = 5000

def receber_mensagem(sock):
    """Thread que recebe mensagens do servidor."""
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("Conexão encerrada pelo servidor")
                break
            
            print('\n' + data.decode())
        
        except:
            break
        
# Cria um socket TCP usando IPv4 (AF_INET) e SOCK_STREAM (TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) # Conecta ao servidor especificado pelo HOST e PORT
    print("Conectado ao servidor!")

    # Thread para receber mensagens
    thread = threading.Thread(target=receber_mensagem, args=(s,))
    thread.daemon = True
    thread.start()

    # Loop para enviar mensagens
    while True:
        msg = input()

        # Envia a mensagem
        s.sendall(msg.encode())

        # Comando de saída
        if msg.lower() == "sair":
            print("Você saiu do chat.")
            break