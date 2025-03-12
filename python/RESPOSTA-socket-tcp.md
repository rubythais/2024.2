# Atividade Sistemas Operacionais (servidor TCP)
- Aluna; Tâmara Thais Lourenço de Carvalho
- Matricula: 20232014040040 

# Tutorial de um Servidor TCP Simplificado em Python


## 1. Socket Server

Nesse tutorial a gente vai criar um servidor TCP simples em Python usando o módulo `socketserver`. Esse servidor vai receber dados de um cliente, exibir no console o que recebeu e, em seguida, devolver os dados em letras maiúsculas.

### Passo 1: Importar o Módulo `socketserver`

Primeiro, precisamos importar o módulo `socketserver`, que facilita a criação de servidores de rede:

```python
import socketserver
```

### Passo 2: Criar a Classe Manipuladora de Requisições

Agora, criamos ums classe para lidar com as conexões dos clientes. Sempre que um cliente se conectar, essa classe vai receber os dados, exibir no console e devolver a mensagem em maiúsculas.

```python
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("Recebido de {}:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())
```

### Passo 3: Configurar e Iniciar o Servidor

Agora, configuramos o servidor para rodar eouvir conexões na porta especificada.

```python
if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 8080  # Alterado p rodar localmente
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
```

 **Dicas p testar localmente:**

- Se você estiver rodando o servidor no mesmo computador, use `127.0.0.1` no lugar do IP real.
- Certifique-se de que a porta escolhida (no exemplo, `8080`) não está sendo usada por outro processo.
- Sempre inicie o servidor antes de rodar o cliente.

---

## 2. Socket Cliente

Agora, aqui vamos criar um cliente TCP que se conecta ao servidor, envia dados e recebe a resposta modificada.

### Passo 1: Importar os Módulos Necessários

Precisamos dos módulos `socket` e `sys` para gerenciar conexões e argumentos de linha de comando.

```python
import socket
import sys
```

### Passo 2: Definir o Endereço do Servidor e os Dados a Serem Enviados

Definimos o IP e a ports do servidor para onde o cliente vai se conectar:

```python
HOST, PORT = "127.0.0.1", 8080  # tem que ser igual ao do servidor

data = " ".join(sys.argv[1:])  # captura os argumentos passados na linha de comando
```

### Passo 3: Criar o Socket e Enviar Dados

Criamos um socket TCP, conectamos ao servidor, enviamos a mensagem e aí recebemos a resposta.

```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")

print("Enviado:  {}".format(data))
print("Recebido: {}".format(received))
```

 **Dicas p testar localmente:**

- Vc vai rodar primeiro o servidor e deixar ele ativo.
- Depois, no terminal, execute o cliente com um texto de teste:
  ```sh
  python cliente.py "mensagem de teste"
  ```
- O servidor deve exibir a mensagem e devolver a resposta em maiúsculas.

Com isso, temos um servidor TCP funcional e um cliente que interage com ele.

