>DISCENTES: Evelen Pinheiro de Oliveira e Marcos Eduardo da Silva Braga
>EXERCÍCIO 09 - Captura de tráfego DHCP pelo Wireshark

###### Os dados foram mascarados para proteção

## Visão Geral

* **Cliente (Evelen):** `XX:XX:XX:XX:XX:XX`
* **Servidor DHCP (ZTE):** `YY:YY:YY:YY:YY:YY` / `192.168.1.X`
* **ID da Transação:** `0x`

### Pacote 1: DHCP Request

* **Tipo de Mensagem:** **DHCP Request (3)**
* **Camada 2 (Ethernet):**
    * **MAC de Origem:** (Cliente `Evelen`)
    * **MAC de Destino:** `Broadcast (ff:ff:ff:ff:ff:ff)`
* **Camada 3 (IP):**
    * **IP de Origem:** `0.0.0.0` 
    * **IP de Destino:** `255.255.255.255` 
* **Camada 4 (UDP):**
    * **Porta de Origem:** `68` (Cliente DHCP)
    * **Porta de Destino:** `67` (Servidor DHCP)
* **Detalhes do DHCP:**
    * **IP Solicitado:** O cliente pede para usar o IP `192.168.1.X`
    * **Nome do Host:** `Evelen`

### Pacote 2: DHCP ACK

* **Tipo de Mensagem:** **DHCP ACK (5)** 
* **Camada 2 (Ethernet):**
    * **MAC de Origem:** (Servidor DHCP)
    * **MAC de Destino:** `Broadcast (ff:ff:ff:ff:ff:ff)`
* **Camada 3 (IP):**
    * **IP de Origem:** `192.168.1.X` 
    * **IP de Destino:** `255.255.255.255` 
* **Camada 4 (UDP):**
    * **Porta de Origem:** `67` (Servidor DHCP)
    * **Porta de Destino:** `68` (Cliente DHCP)
* **Detalhes do DHCP (A "Configuração"):**
    * **IP Fornecido:** `192.168.1.X` (O IP que o cliente `Evelen` agora pode usar)
    * **Tempo de "Aluguel":** `1 dia (86400 segundos)`
    * **Identificador do Servidor:** `192.168.1.X`
    * **Opções Fornecidas ao Cliente:**
        * **Máscara de Sub-rede:** `255.255.255.0`
        * **Roteador (Gateway):** `192.168.1.X`