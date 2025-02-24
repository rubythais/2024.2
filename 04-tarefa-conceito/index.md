# Conceito de tarefas

## Informações gerais

- Capítulo: [Conceito de tarefas](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-04.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: Tâmara Thais Lourenço de Carvalho
- matrícula: 20232014040040

## Respostas dos exercícios:

1. O time sharing divide o tempo do processador entre as tarefas, evitando que ele fique parado e garantindo que o sistema continue funcionando sem travamentos.

2. A duração do quatum e fatia de tempo, é variada de acordo com o sistema operacional. 
Exemplo: o linux demora de 10 a #00 milissegundos enquanto o windows demora de 1 a 200 milissegundos a depender do tipo de tarefa.


4. E → P - É possível quando ocorre o fim do quantum.

E → S - É possível quando um recurso indisponível é solicitado.  

S → E - Não é possível.

P → N - Não é possível.

S → T - Não é possível.

S → P - É possível ao contrário do E → S ela é possível quando o recurso solicitado está disponível.

E → T - É possível quando a tarefa é encerrada, tanto por ser concluída quanto por ter ocorrido algum tipo de erro.

N → S - Nnão é possível.

P → S - Não é possível.

5. P → P → N → T → S → P → S → N → E → S
