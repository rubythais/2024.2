# Respostas: Tutorial Criando um Servidor TCP Simples em Python

### Informações Gerais
- **Público alvo**: alunos da disciplina de SO (Sistemas Operacionais) do curso de TADS (Superior em Tecnologia em Análise e Desenvolvimento de Sistemas) no CNAT-IFRN (Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte - Campus Natal-Central).
- **Disciplina**: SO (Sistemas Operacionais)
- **Professor**: [Leonardo A. Minora](https://github.com/leonardo-minora)
- **Texto gerado por**: [Microsoft Copilot](https://copilot.microsoft.com/)

## Respostas e Explicações

### 1. Criando um Servidor TCP Simples

#### Enunciado
Crie um servidor TCP simples usando o módulo `socketserver` que:
- Receba dados de um cliente.
- Imprima os dados recebidos no console.
- Envie os dados de volta em letras maiúsculas.

#### Resposta

**Passo 1: Importar o Módulo `socketserver`**
```python
import socketserver
```

**Passo 2: Criar a Classe Manipuladora de Requisições**
```python
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    A classe manipuladora de requisições para nosso servidor.

    Ela é instanciada uma vez por conexão ao servidor e deve
    sobrescrever o método handle() para implementar a comunicação
    com o cliente.
    """

    def handle(self):
        # self.request é o socket TCP conectado ao cliente
        self.data = self.request.recv(1024).strip()
        print("Recebido de {}:".format(self.client_address[0]))
        print(self.data)
        # apenas envia de volta os mesmos dados, mas em maiúsculas
        self.request.sendall(self.data.upper())
```

**Passo 3: Configurar e Iniciar o Servidor**
```python
if __name__ == "__main__":
    HOST, PORT = "10.25.2.25", 80

    # Criar o servidor, vinculando ao endereço e porta especificados
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Ativar o servidor; isso manterá o servidor rodando até que
        # você interrompa o programa com Ctrl-C
        server.serve_forever()
```

**Explicação**:
- `socketserver.BaseRequestHandler`: Cria uma classe que gerencia cada conexão.
- `recv(1024)`: Recebe até 1024 bytes de dados do cliente.
- `sendall(data.upper())`: Envia os dados de volta em letras maiúsculas.
- `TCPServer((HOST, PORT), MyTCPHandler)`: Configura o servidor no endereço e porta especificados.

### 2. Criando um Cliente TCP Simples

#### Enunciado
Crie um cliente TCP que:
- Conecte-se a um servidor.
- Envie uma mensagem ao servidor.
- Receba uma resposta do servidor.

#### Resposta

**Passo 1: Importar os Módulos Necessários**
```python
import socket
import sys
```

**Passo 2: Definir o Endereço do Servidor e os Dados a Serem Enviados**
```python
HOST, PORT = "10.25.2.25", 80
data = " ".join(sys.argv[1:])
```

**Passo 3: Criar o Socket e Conectar ao Servidor**
```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Conectar ao servidor e enviar dados
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receber dados do servidor e encerrar
    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))
```

**Explicação**:
- `socket.AF_INET`: Usa IPv4.
- `socket.SOCK_STREAM`: Indica TCP.
- `connect((HOST, PORT))`: Conecta ao servidor no endereço e porta especificados.
- `sendall()`: Envia dados para o servidor.
- `recv(1024)`: Recebe até 1024 bytes de dados do servidor.

### 3. Links Relevantes

- [Documentação Oficial: socketserver](https://docs.python.org/3/library/socketserver.html)

## Código Completo

### Servidor TCP
```python
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("Recebido de {}:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "10.25.2.25", 80

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
```

### Cliente TCP
```python
import socket
import sys

HOST, PORT = "10.25.2.25", 80
data = " ".join(sys.argv[1:])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))
```
