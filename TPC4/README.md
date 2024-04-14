# TP4: Analisador Léxico


## Autor
- Benjamim Meleiro Rodrigues
- A93323

## Objetivos
O objetivo deste TPC é construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:
> Select id, nome, salario From empregados Where salario >= 820


## Resolução

Para resolver este TPC, o primeiro passo é definir os tokens necessários para a análise léxica da linguagem de query. Neste caso, precisamos de tokens como SELECT, FROM, WHERE, IDENTIFIER, OPERATOR, COMMA e NUMBER.

Em seguida, utilizei expressões regulares para definir as regras de reconhecimento de cada token, defini regras para ignorar espaços em branco e tabulações, uma vez que não têm significado na linguagem de query, e, para além disso, defini uma regra para reconhecer novas linhas e atualizar o número de linha do lexer.

Para lidar com erros de token, implementei uma função que imprime uma mensagem de erro e ignora o caractere inválido.

Utilizando a biblioteca Ply (Python Lex-Yacc), construímos o analisador léxico.

Finalmente, testamos o analisador léxico fornecendo-lhe a string de teste que contém a query. O analisador identifica e imprime cada token encontrado na string.
