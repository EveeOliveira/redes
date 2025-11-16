>DISCENTES: Evelen Pinheiro de Oliveira e Marcos Eduardo da Silva Braga
>EXERCÍCIO 07 - Captura de tráfego DNS pelo Wireshark

## Pacote 292: DNS Request

* **Hora da Captura:** Nov 16, 2025
* **Tamanho do Pacote:** 77 bytes
* **Dispositivo de Origem:** `192.168.1.100`
* **Dispositivo de Destino:** `8.8.8.8`

### 1. Resolução de Nome (Query)

* **Pacote Nº:** `292`  
* **Transaction ID:** `0x506d`  
* **Flags:** `0x0100 Standart query`
* **Questions:** `1`
* **Queries:** `www.google.com.br: type A, class IN`

### 2. Resolução de Nome (Response)

* **Pacote Nº:** `294`  
* **Transaction ID:** `0x506d` 
* **Flags:** `0x8180 Standart query response`
* **Questions:** `1`
* **Answer RRs:** `1`
* **Queries:** `www.google.com.br: type A, class IN`
* **Answers:** `www.google.com.br: type A, class IN, addr 172.217.28.131`

### 3. DNS Utilizado

* **DNS google:** `8.8.8.8`
* **Registro de DNS:** `Tópico 1 e 2`
