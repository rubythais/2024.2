# Implementação de tarefas

## Informações gerais

- Capítulo: [Implementação de tarefas](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-05.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: Tâmara Thais Lourenço de Carvalho
- matrícula: 20232014040040

## Respostas dos exercícios

### Exercício 7: Soma com 4 Tarefas (Usando Threads)

```python
import threading

class MinhaThread(threading.Thread):
    def __init__(self, numeros):
        threading.Thread.__init__(self)
        self.numeros = numeros
        self.resultado = 0

    def run(self):
        self.resultado = sum(self.numeros)

def ler_numeros_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        numeros = [int(linha.strip()) for linha in arquivo]
    return numeros

nome_arquivo = 'numeros_aleatorios.txt'
numeros = ler_numeros_do_arquivo(nome_arquivo)

tamanho_parte = len(numeros) // 4
partes = [numeros[i * tamanho_parte:(i + 1) * tamanho_parte] for i in range(4)]

threads = [MinhaThread(parte) for parte in partes]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

resultado_final = sum(thread.resultado for thread in threads)
print(f"A soma dos números com 4 tarefas é: {resultado_final}")
