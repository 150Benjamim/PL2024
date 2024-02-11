# TPC

O objetivo deste TPC é analisar um conjunto de dados sem usar o módulo CSV, criando uma lista ordenada das modalidades desportivas, calculando as percentagens de atletas aptos e inaptos, e determinando a distribuição dos atletas por faixas etárias de 5 anos.

Para isto defini uma função chamada parse_csv que lê um arquivo CSV e extrai informações relevantes para três estruturas de dados: um dicionário (emd_dict), um conjunto (modalidades), e outro dicionário (escaloes).

- O dicionário emd_dict armazena informações sobre os atletas indexados por seu _id. 
- O conjunto modalidades armazena todas as modalidades desportivas encontradas no arquivo CSV. 
- O dicionário escaloes armazena a distribuição dos atletas por faixas etárias, onde as chaves são os escalões e os valores são o número de atletas em cada escalão.

A função parse_csv recebe como input o caminho do ficheiro CSV, o dicionário emd_dict, o conjunto modalidades e o dicionário escaloes. A função processa o ficheiro CSV, preenchendo a cada linha lida as estruturas de dados conforme descrito anteriormente e retorna o número de atletas aptos.

De forma a imprimir os resultados defini três funções adicionais: print_modalidades, print_atletas_aptos e print_escaloes. Estas funções recebem os dados processados pelas funções anteriores e imprimem informações sobre as modalidades desportivas, a percentagem de atletas aptos em relação ao total de atletas e a distribuição dos atletas por faixas etárias, respectivamente.
