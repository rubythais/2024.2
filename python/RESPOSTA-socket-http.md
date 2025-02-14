# Atividade Sistemas Operacionais (Socket http)
- Aluna; Tâmara Thais Lourenço de Carvalho
- Matricula: 20232014040040
# Respostas 
## **Atividade 1: Servidor HTTP sem thread**

### **Enunciado**
- **Passo 1:** Executar o servidor HTTP sem thread (código da seção 2.1).
- **Passo 2:** Executar o cliente (código da seção 2.3) para os seguintes casos:
  - 1 cliente
  - 2 clientes simultâneos
  - 5 clientes simultâneos
  - 10 clientes simultâneos
- **Passo 3:** Analisar e explicar o comportamento do cliente e do servidor sem thread para cada caso.

### **Código do Servidor HTTP sem thread (Exemplo)**

```python
import socket

def servidor_http():
    host = 'localhost'
    porta = 8080
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(5)
    
    print(f"Servidor rodando em {host}:{porta}... Aguardando conexões.")
    
    while True:
        conexao, endereco = servidor.accept()
        print(f"Conexão recebida de {endereco}")
        
        # Requisição
        requisicao = conexao.recv(1024)
        print(f"Requisição recebida:\n{requisicao.decode()}")
        
        # Enviar resposta
        resposta = """HTTP/1.1 200 OK\nContent-Type: text/html\n\n
                      <html><body><h1>Olá, mundo!</h1></body></html>"""
        conexao.sendall(resposta.encode())
        conexao.close()

if __name__ == '__main__':
    servidor_http()
```

### **Código do Cliente (Exemplo)**

```python
import socket

def cliente_http():
    host = 'localhost'
    porta = 8080
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    cliente.connect((host, porta))
    
    requisicao = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    cliente.sendall(requisicao.encode())
    
    resposta = cliente.recv(1024)
    print("Resposta do servidor:")
    print(resposta.decode())
    
    cliente.close()

if __name__ == '__main__':
    cliente_http()
```

### **Comportamento do Servidor sem Thread**
- O servidor irá processar cada requisição de cliente uma por vez. Portanto, quando você testar com múltiplos clientes simultâneos (2, 5 ou 10), eles precisarão esperar na fila enquanto o servidor responde a um cliente por vez.
- Com 10 clientes simultâneos, o servidor irá processar o primeiro cliente, depois o segundo, e assim por diante. Isso causará atrasos, já que as requisições são processadas de forma sequencial.

---

## **Atividade 2: Servidor HTTP com thread**

### **Enunciado**
- **Passo 1:** Pare o servidor sem thread e execute o servidor HTTP com thread (código da seção 2.2).
- **Passo 2:** Execute o cliente (código da seção 2.3) para os seguintes casos:
  - 1 cliente
  - 2 clientes simultâneos
  - 5 clientes simultâneos
  - 10 clientes simultâneos
- **Passo 3:** Analisar e explicar o comportamento do cliente e do servidor com thread para cada caso.

### **Código do Servidor HTTP com Thread (Exemplo)**

```python
import socket
import threading

def tratar_cliente(conexao, endereco):
    print(f"Conexão recebida de {endereco}")
    requisicao = conexao.recv(1024)
    print(f"Requisição recebida:\n{requisicao.decode()}")
    
    resposta = """HTTP/1.1 200 OK\nContent-Type: text/html\n\n
                  <html><body><h1>Olá, mundo!</h1></body></html>"""
    conexao.sendall(resposta.encode())
    conexao.close()

def servidor_http():
    host = 'localhost'
    porta = 8080
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(5)
    
    print(f"Servidor rodando em {host}:{porta}... Aguardando conexões.")
    
    while True:
        conexao, endereco = servidor.accept()
        # Criando thread para cada cliente
        thread = threading.Thread(target=tratar_cliente, args=(conexao, endereco))
        thread.start()

if __name__ == '__main__':
    servidor_http()
```

### **Código do Cliente (Exemplo)**

```python
import socket

def cliente_http():
    host = 'localhost'
    porta = 8080
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    cliente.connect((host, porta))
    
    requisicao = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    cliente.sendall(requisicao.encode())
    
    resposta = cliente.recv(1024)
    print("Resposta do servidor:")
    print(resposta.decode())
    
    cliente.close()

if __name__ == '__main__':
    cliente_http()
```

### **Comportamento do Servidor com Thread**
- Com o servidor utilizando threads, ele pode atender várias requisições simultaneamente. Isso melhora a performance ao lidar com múltiplos clientes ao mesmo tempo, pois o servidor cria uma nova thread para cada requisição, permitindo o processamento simultâneo.
- Mesmo com 10 ou mais clientes simultâneos, o servidor será capaz de responder a todos eles de forma rápida, pois as threads são tratadas de maneira independente, evitando que o servidor precise esperar para processar uma requisição de cada vez.

---

## **Explicação das Diferenças Observadas**

1. **Servidor sem thread:**
   - **Vantagens:** Simples de implementar e entender.
   - **Desvantagens:** O servidor processa uma requisição por vez. Com múltiplos clientes, isso leva a uma fila de espera, aumentando o tempo de resposta.

2. **Servidor com thread:**
   - **Vantagens:** Cada cliente é atendido de maneira simultânea em uma nova thread. O servidor pode processar várias requisições ao mesmo tempo, o que melhora a performance e reduz os tempos de espera.
   - **Desvantagens:** Pode haver um aumento no uso de memória e recursos do sistema, já que várias threads são criadas para processar múltiplos clientes simultaneamente.

