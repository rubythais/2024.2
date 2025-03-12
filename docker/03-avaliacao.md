# Docker Compose com Django e Banco de Dados

## Informações Gerais

- **Assunto:** Docker, conteinerizar aplicativos
- **Disciplina:** *Sistemas Operacionais*
- **Tarefa:**
  1. Criar um projeto Django com uma aplicação web
     - Alternativa: Criar uma *branch* no repositório do projeto integrador para configurar o acesso ao repositório de dados
  2. Criar um `Dockerfile` para o projeto Django
  3. Criar a imagem e testar o contêiner
  4. **OPCIONAL:** Criar um `Dockerfile` para o repositório de banco de dados
  5. Criar um `docker-compose.yml` e configurar para 2 serviços: `webapp` e `db`
  6. Configurar o arquivo Django de acesso ao repositório de dados para usar o serviço Docker `db`
  7. Testar o `docker-compose.yml`
  8. Relatar minimamente o que foi feito.
- **Entrega:** Cópia deste arquivo Markdown preenchido, no seu repositório *fork* de [https://github.com/sistemas-operacionais/2024.2](https://github.com/sistemas-operacionais/2024.2)

---

## Relatório

### Aluno

- **Nome:** Tâmara Thais Lourenço de Carvalho
- **Matrícula:** 20232014040040

### Etapas do Processo

Não tinha um projeto de PDS, então me juntei ao grupo responsável pelo projeto **Arkheion** para conseguir realizar a atividade.

1. **Configuração do Projeto**
   - Inicialmente, trouxemos o arquivo `requirements.txt` para o diretório `mysite`, onde está o projeto Django.
   - O arquivo original continha cerca de **600\~700 linhas**, o que dificultava a identificação das dependências essenciais.
   - Utilizamos o **Deepseek** para sugerir uma versão otimizada do arquivo, mantendo apenas as dependências necessárias.

2. **Criação dos Arquivos Docker**
   - Após ajustar o `requirements.txt`, criamos os arquivos `Dockerfile` e `docker-compose.yml`.

3. **Testes e Correções**
   - Executamos o comando `docker-compose up --build` para iniciar e construir o contêiner.
   - No primeiro teste, houve um erro ao copiar o `requirements.txt`.
   - Após a correção, o comando foi executado corretamente, utilizando:
     ```bash
     bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
     ```
     - Esse comando garante a execução das migrações do banco de dados e inicia o servidor Django.

---

## Arquivos Docker e Configuração do Django

### Arquivo: `Dockerfile`

```dockerfile
FROM python:3.12
WORKDIR /mysite
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

### Arquivo: `docker-compose.yml`

```yaml
version: '3.8'
services:
  webapp:
    build: .
    container_name: arkheion_webapp
    command: bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=${DATABASE_URL}
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data/
volumes:
  postgres_data:
```

### Comandos Utilizados

1. **Criar o arquivo `requirements.txt`**
   ```bash
   pip freeze > requirements.txt
   ```

2. **Construir a imagem Docker**
   ```bash
   docker build --no-cache -t arkheion .
   ```

3. **Executar o container diretamente**
   ```bash
   docker run -p 8000:8000 arkheion
   ```

4. **Executar com volumes**
   ```bash
   docker run -it -v /local:/app -p 8000:8000 arkheion
   ```

5. **Executar o Docker Compose**
   ```bash
   docker-compose up --build
   ```

---

## Observações e Conclusão

- A otimização do `requirements.txt` foi essencial para evitar erros e melhorar a eficiência da instalação das dependências.
- Os arquivos `Dockerfile` e `docker-compose.yml` foram configurados e testados para garantir o funcionamento correto do projeto.
- O uso do `docker-compose` permitiu automatizar a execução do servidor e a aplicação das migrações do banco de dados.

Caso precise de mais ajustes, estou à disposição! 🚀

