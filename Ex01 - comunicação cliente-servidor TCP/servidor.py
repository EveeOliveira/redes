'''
DISCENTES: Evelen Pinheiro de Oliveira e Marcos Eduardo da Silva Braga
EXERCÍCIO 01 - COMUNICAÇÃO CLIENTE-SERVIDOR COM PROTOCOLO TCP

'''
import socket

HOST = '127.0.0.1'    # Endereço IP onde o servidor vai rodar (localhost)
PORT = 5000           # Porta em que rodará a aplicação

# Cria um socket TCP usando IPv4 (AF_INET) e SOCK_STREAM (TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))    # Cria a associação do socket com o endereço e porta
    s.listen()              # Deixa o servidor rodando em modo de escuta
    print(f'Servidor rodando em {HOST}:{PORT}')

    conn, addr = s.accept() # Aguarda até que algum cliente tente se conectar
    with conn:  
        print(f'Conexão por {addr}')
        while True:                         # Loop que mantém o servidor recebendo mensagens do cliente
            data = conn.recv(1024)          # Recebe até 1024 bytes de dados
            if not data:                    # Se 'data' vier vazio, significa que o cliente desconectou
                break
            
            print(f'Mensagem recebida: {data.decode()}')
            resposta = 'Recebido! Mensagem: ' + data.decode()
            conn.sendall(resposta.encode()) # Envia a resposta codificada para o cliente

    # Fecha conexão e o socket
    conn.close()
    s.close()
    print(f'Servidor desligado')