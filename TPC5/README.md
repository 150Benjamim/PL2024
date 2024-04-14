# TP5: Máquina de Vending


## Autor
- Benjamim Meleiro Rodrigues
- A93323

## Objetivos
O objetivo deste TPC é construir um programa que simule uma máquina de vending.

## Resolução

Primeiro, carreguei os dados do arquivo JSON com as informações do stock. Depois, comecei a definir as funções necessárias para lidar com as transações de compra e troco, bem como para converter valores de moeda para inteiros e vice-versa.

Criei as regras e tokens para o analisador léxico usando a biblioteca ply.lex, especificando padrões para os comandos que o usuário pode inserir, como "LISTAR", "MOEDA", "VALOR", "SELECIONAR", "COD" e "SAIR". Também defini padrões para ignorar espaços em branco, tabulações e quebras de linha.

Depois disso, implementei a lógica principal do programa dentro do loop principal. O programa fica à espera de comandos do utilizar e executa a ação correspondente a cada comando reconhecido.
O programa sai deste loop quando o input do utilizador é "SAIR".

Finalmente, as alterações do stock são guardadas no arquivo JSON de forma a manter o stock atualizado.
