import socketserver

class ManipuladorTCP(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            # Recebe os dados do cliente
            dados = self.request.recv(1024).strip()
            print(f"[LOG] Mensagem recebida de {self.client_address[0]}: {dados.decode()}")
            
        
            resposta = dados.upper()
            self.request.sendall(resposta)
            print("[LOG] Resposta enviada.")
        except Exception as e:
            print(f"[ERRO] Problema ao processar requisição: {e}")

if __name__ == "__main__":
    HOST, PORTA = "127.0.0.1", 8080  # aqui estou garantindo que seja um endereço suportado
    
    try:
        with socketserver.TCPServer((HOST, PORTA), ManipuladorTCP) as servidor:
            print(f"Servidor rodando em {HOST}:{PORTA}... Pressione Ctrl+C para parar.")
            servidor.serve_forever()
    except OSError as e:
        print(f"[ERRO] Não foi possível iniciar o servidor: {e}")
