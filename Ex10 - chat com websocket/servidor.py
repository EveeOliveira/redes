import asyncio
import websockets

# Conjunto que armazenará todos os clientes conectados ao servidor
clientes = set()

# Função que será chamada sempre que um novo cliente se conectar ao servidor
async def handler(websocket):
    # Adiciona o cliente recém-conectado ao conjunto de clientes
    clientes.add(websocket)
    print("Novo cliente conectado!")

    try:
        # Loop que aguarda continuamente mensagens enviadas pelo cliente
        async for message in websocket:
            print(f"Mensagem recebida: {message}")

            # Envia a mensagem recebida para todos os clientes conectados
            for cliente in clientes:
              # Excluir do envio o cliente que enviou a mensagem
              if cliente != websocket:
                await cliente.send(message)

    # Caso o cliente desconecte (feche a conexão), é levantada uma exceção
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectado.")
    finally:
        # Remove o cliente do conjunto para evitar referências inválidas
        clientes.remove(websocket)

# Função principal que inicia o servidor WebSocket
async def main():
    print("Servidor WebSocket rodando na porta 8765...")
    # Cria o servidor WebSocket e o mantém ativo
    async with websockets.serve(handler, "0.0.0.0", 8765):
        # Mantém a aplicação rodando indefinidamente
        await asyncio.Future()

# Executa o servidor
asyncio.run(main())
