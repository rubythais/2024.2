import http.client
import threading
import time

def fazer_requisicao_get():
    conexao = http.client.HTTPConnection("localhost", 8000)

    conexao.request("GET", "/")

    
    resposta = conexao.getresponse()

    conteudo = resposta.read()

    print(f"Status: {resposta.status}")
    print(f"Motivo: {resposta.reason}")
    print("Conteúdo:")
    print(conteudo.decode("utf-8"))

    conexao.close()


def rodar_clientes(numero_de_clientes):
    threads = []

    for i in range(numero_de_clientes):
        t = threading.Thread(target=fazer_requisicao_get())
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    numero_de_clientes = int(input())
    start_time = time.time()
    rodar_clientes(numero_de_clientes)
    print(f"\nCom {numero_de_clientes} demorou: {time.time() - start_time}")
