from concurrent.futures import ThreadPoolExecutor

def ler_numeros_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        numeros = [int(linha.strip()) for linha in arquivo]
    return numeros

def soma_numeros(numeros):
    return sum(numeros)

nome_arquivo = 'numeros_aleatorios.txt'
numeros = ler_numeros_do_arquivo(nome_arquivo)

tamanho_parte = len(numeros) // 10
partes = [numeros[i * tamanho_parte:(i + 1) * tamanho_parte] for i in range(10)]

with ThreadPoolExecutor(max_workers=10) as executor:
    futuros = [executor.submit(soma_numeros, parte) for parte in partes]
    resultados = [futuro.result() for futuro in futuros]

resultado_final = sum(resultados)
print(f"A soma dos números com 10 tarefas é: {resultado_final}")
