>DISCENTES: Evelen Pinheiro de Oliveira e Marcos Eduardo da Silva Braga
>EXERCÍCIO 06 - Captura de tráfego TCP pelo Wireshark

### 1. Conexão

* **5:** `Local IP -> Destination | TCP | Source Port: 50922 -> Destination Port: 80 | [SYN]`
* **6:** `Destination -> Local IP | TCP | Source Port: 80    -> Destination Port: 80 | [SYN, ACK]`
* **7:** `Local IP -> Destination | TCP | Source Port: 50922 -> Destination Port: 80 | [ACK]`

### 2. Encerramento

* **17:** `Destination -> Local IP | TCP | Source Port: 80    -> Destination Port: 80 | [FIN, ACK]`
* **18:** `Local IP -> Destination | TCP | Source Port: 50922 -> Destination Port: 80 | [ACK]`
* **19:** `Local IP -> Destination | TCP | Source Port: 50922 -> Destination Port: 80 | [FIN, ACK]`
* **20:** `Destination -> Local IP | TCP | Source Port: 80    -> Destination Port: 80 | [ACK]`
