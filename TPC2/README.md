# TPC2: Pequeno Conversor de MarkDown para HTML

## Autor
- Benjamim Meleiro Rodrigues
- A93323

## Objetivos
O objetivo deste TPC é criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da ![Cheat Sheet](https://www.markdownguide.org/cheat-sheet/):


## Resolução
Comecei por identificar os elementos do MarkDown que precisavam de ser convertidos para HTML, baseando-me na "Basic Syntax" da Cheat Sheet. De seguida, defini uma função principal, markdown_to_html, onde tratei cada elemento MarkDown individualmente usando expressões regulares para substituir o texto Markdown correspondente pelo HTML equivalente.

Tratei de cabeçalhos, negrito, itálico, citações em bloco, imagens, links, regras horizontais, código, listas ordenadas e não ordenadas. Para as listas, dividi o processamento em dois estágios: primeiro, identificando a lista em si e depois os itens da lista.

Além disso, implementei uma função auxiliar, wrap_in_paragraph, para envolver o conteúdo em parágrafos HTML, caso necessário. Por fim, criei o esqueleto básico do HTML, abrindo e fechando as tags <html>, <body> etc., e escrevi o conteúdo HTML resultante num ficheiro de saída.
