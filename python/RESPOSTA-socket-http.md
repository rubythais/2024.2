# Atividade Sistemas Operacionais (Socket http)
- Aluna; Tâmara Thais Lourenço de Carvalho
- Matricula: 20232014040040
# Respostas 
# Análise do Servidor HTTP: Com e Sem Threads.

## 1. Experimento 1

### Servidor HTTP sem Threads

#### Testes e Análises:

1. **Apenas 1 clientwe**

   - O servidor atende a requisição normalmente.
   - A resposta é enviada rapidamente, sem atrasos.
   - O cliente recebe a página HTML fixa corretamente.

2. **2 clientes simultaneos**

   - O primeiro cliente é atendido imediatamente.
   - O segundo cliente tem que esperar a finalização do primeiro.
   - Pequeno atraso para o segundo cliente.

3. **5 clientes simultâneos**

   - O servidor processa as requisições uma por uma.
   - Os clientes esperam em fila.
   - A latência para os últimos aumenta de forma considerável.

4. **10 clientes simultâneos**

   - A fila fica longa e a espera para os últimos clientes é bem alta.
   - Como o servidor só consegue lidar com um cliente por vez, o tempo de resposta cresce muito.

### Servidor HTTP com Threads

#### Testes e Análises:

1. **Apenas 1 cliente**

   - Funciona como no servidor sem thread, a resposta é rápida.
   - O cliente recebe o conteúdo sem demora.

2. **2 clientes simultâneos**

   - Ambos são atendidos ao mesmo tempo, pois cada um tem sua própria thread.
   - O tempo de resposta para o segundo cliente é praticamente igual ao do primeiro.

3. **5 clientes simultâneos**

   - O servidor trata várias requisições ao mesmo tempo.
   - O tempo de resposta é menor para todos.

4. **10 clientes simultâneos**

   - O servidor distribui as requisiçoes entre as threads.
   - O tempo de resposta é bem menor comparado ao servidor sem thread.

## 2. Comparando Servidor com e sem Threads

| Clientes Simultâneos | Servidor Sem Thread                  | Servidor Com Thread                            |
| -------------------- | ------------------------------------ | ---------------------------------------------- |
| 1                    | Atendimento rápido                   | Atendimento rápido                             |
| 2                    | O segundo espera o primeiro terminar | Ambos atendidos ao mesmo tempo                 |
| 5                    | Filas e tempo de resposta maior      | Processamento simultâneo, tempo menor          |
| 10                   | Tempp de espera muito alto           | Threads atendem vários clientes ao mesmo tempo |

### Diferença no Funcionamento:

- **Servidor sem threads:** Atende um cliente por vez, como um caixa de supermercado com um único atendente para fazer o trablaho.
- **Servidor com threads:** Cada requisição tem sua própria thread, como vários caixas funcionando ao mesmo tempo.
- O uso de threads melhora muito o desempenho e evita filas demoradas.

### Conclusão:

Usar threads é essencial para servidores HTTP que precisam atender vários clientes ao mesmo tempo. Sem threads, as requisições ficam presas em fila, aumentando o tempo de espera. Com threads, cada requisição é tratada separadamente, tornando o servidor mais eficiente e escalável.


