# Chat WebSocket em Python (Terminal)

Este projeto implementa um **chat em tempo real no terminal**, utilizando **WebSockets**, **asyncio** e **Python 3**.  
O chat permite que vários clientes enviem e recebam mensagens simultaneamente usando a biblioteca `websockets`.

---

## Funcionalidades

- ✔ Comunicação em tempo real  
- ✔ Múltiplos clientes conectados  
- ✔ Envio e recebimento simultâneos (via asyncio)  
- ✔ Comando de saída (`sair`)  

---

## Pré-requisitos

Certifique-se de ter instalado:

- **Python 3.10+**
- **pip**

Verifique com:

```bash
python3 --version
pip --version
```

---

## Instalação

No diretório do projeto, execute:
```
python3 -m venv .venv
```

Depois ative o ambiente virtual:
```
source .venv/bin/activate
```

E por fim instale a dependência:
```
pip install websockets
```

---

## Execução

Com o ambiente virtual ativo, rode em um terminal o arquivo 'servidor.py' e em diferentes outros, o arquivo 'cliente.py'.
Rodar o servidor:
```
python3 servidor.py
```

Rodar o cliente:
```
python3 cliente.py
```