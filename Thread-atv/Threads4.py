import threading
import random

class MinhaThread(threading.Thread):
    def __init__(self, numeros):
        threading.Thread.__init__(self)
        self.numeros = numeros
        self.resultado = 0

    def run(self):
        self.resultado = soma_numeros(self.numeros)

# 1. Função para transferir números do arquivo para uma lista
def ler_numeros_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        numeros = [int(linha.strip()) for linha in arquivo]
    return numeros

# 2. Funçao para somar números de uma lista
def soma_numeros(numeros):
    return sum(numeros)

# 3. Chama a função para transferir números para lista
nome_arquivo = 'numeros_aleatorios.txt'
numeros = ler_numeros_do_arquivo(nome_arquivo)

# 4. Divide a lista em 2 partes
metade = len(numeros) // 2
numeros_parte_1 = numeros[0:len(numeros) // 4]
numeros_parte_2 = numeros[len(numeros) // 4: len(numeros) // 2]
numeros_parte_3 = numeros[len(numeros) // 2: (len(numeros) // 4) * 3]
numeros_parte_4 = numeros[(len(numeros) // 4) * 3:]
resultados = [0, 0, 0, 0, ]
# 1 2 3 4 5 6 7 8 
# 5. Cria 2 tarefas, cada uma com uma parte da lista de números
thread_1 = MinhaThread(numeros_parte_1)
thread_2 = MinhaThread(numeros_parte_2)
thread_3 = MinhaThread(numeros_parte_3)
thread_4 = MinhaThread(numeros_parte_4)

# 6. Executa as 2 tarefas

### Solicita execução do método run() da thread
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

### Sguarda o fim da execução do método run() da thread
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
### Recupera valor do resultado da execução
resultados[0] = thread_1.resultado
resultados[1] = thread_2.resultado
resultados[2] = thread_3.resultado
resultados[3] = thread_4.resultado

# 7. Soma o resultado final e imprime
resultado = soma_numeros(resultados)
print(f"A soma dos números é: {resultado}")
