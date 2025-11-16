import asyncio
import websockets

# Função responsável por ENVIAR mensagens para o servidor
async def enviar(websocket):
    while True:
        # Lê a mensagem digitada pelo usuário no terminal
        msg = input("")
        # Envia a mensagem ao servidor
        await websocket.send(msg)

        # Verifica se o usuário deseja encerrar o chat
        if msg.lower() == "sair":
            print("Encerrando cliente...")
            # Fecha a conexão WebSocket
            await websocket.close()
            break

# Função responsável por RECEBER mensagens do servidor
async def receber(websocket):
    try:
        # Fica aguardando continuamente novas mensagens do servidor
        async for msg in websocket:
            print(f"\nMensagem recebida: {msg}")

    # Caso a conexão seja encerrada, evita erro
    except websockets.exceptions.ConnectionClosed:
        pass

# Função principal que inicia a conexão com o servidor
async def main():
    uri = "ws://localhost:8765" # Endereço do servidor WebSocket

    # Abre a conexão com o servidor
    async with websockets.connect(uri) as websocket:
        print("Conectado ao servidor!")

        # Cria duas tasks: envio e recebimento em paralelo
        task_envio = asyncio.create_task(enviar(websocket))
        task_recebe = asyncio.create_task(receber(websocket))

        # aguarda as tasks terminarem
        await asyncio.wait(
            [task_envio, task_recebe],
            return_when=asyncio.FIRST_COMPLETED
        )

# Executa o programa principal
asyncio.run(main())