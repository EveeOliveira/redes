'''
DISCENTES: Evelen Pinheiro de Oliveira e Marcos Eduardo da Silva Braga
EXERCÍCIO 03 - CHAT EM REDE COM PROTOCOLO TCP

'''
import socket, threading

HOST = '127.0.0.1'    # Endereço IP onde o servidor vai rodar (localhost)
PORT = 5000           # Porta em que rodará a aplicação

clientes = []         # Lista de clientes ativios

def comunicacao_cliente(conn, addr, id_cliente):
    """Thread que escuta as mensagens de um cliente e repassa ao outro."""
    while True: # Loop que mantém o servidor recebendo mensagens do cliente
        try:
            data = conn.recv(1024)  # Recebe até 1024 bytes de dados
            if not data:            # Se 'data' vier vazio, significa que o cliente desconectou
                break
            
            mensagem = data.decode()  # Mensagem recebida do cliente
            if mensagem.lower() == 'sair':  # Desconecta o cliente caso a mensagem seja 'sair'
                print(f'Cliente {id_cliente} saiu')
                conn.sendall('Você saiu do chat'.encode())
                break
            
            print(f'Mensagem do cliente {id_cliente}: {mensagem}')  # Mostra no servidor as mensagens trocadas

            for i, c in enumerate(clientes):  # Transmite as mensagens para todos os cliente conectados
                c.sendall(f'Cliente {id_cliente}: {mensagem}'.encode())

        except:
            break
    
    conn.close()  # Encerra a conexão
    clientes[id_cliente] = None # Desconecta o cliente
    print(f'Cliente {id_cliente} desconectado')

# Cria um socket TCP usando IPv4 (AF_INET) e SOCK_STREAM (TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT)) # Cria a associação do socket com o endereço e porta
    server.listen(2)          # Deixa o servidor rodando em modo de escuta, aceita 2 clientes
    print(f"Servidor aguardando conexões em {HOST}:{PORT}")

    # Aceita exatamente dois clientes
    for i in range(2):
        conn, addr = server.accept()  # Aguarda até que algum cliente tente se conectar
        clientes.append(conn)         # Adiciona o cliente a lista dos clientes ativos

        # Cria a thread para ouvir mensagens deste cliente
        thread = threading.Thread(target=comunicacao_cliente, args=(conn, addr, i))
        thread.start()

    print("Dois clientes conectados. Chat iniciado")