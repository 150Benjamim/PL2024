# TPC3: Somador on/off


## Autor
- Benjamim Meleiro Rodrigues
- A93323

## Objetivos
O objetivo deste TPC é criar um programa em Python que some todas as sequências de dígitos que encontre num texto. Ele para de somar quando encontra "off" e volta a somar quando encontra "on", em qualquer combinação de maiúsculas e minúsculas. Ao encontrar "=", mostra a soma até esse ponto.

## Resolução

**Classe *FiniteStateAutomaton*:**
Para realizar esta tarefa, criei uma classe chamada FiniteStateAutomaton, que representa um Autómato Finito Determinístico. Este autómato pode estar em dois estados, sendo estes "on" ou "off".

Ao criar uma instância desta classe, eu defino os estados possíveis, o estado inicial e os estados de aceitação. O método reset() redefine o autómato para o estado inicial sempre que necessário.

No método process_input(input), eu itero sobre cada elemento do input fornecido. Se encontro "on" ou "off", atualizo o estado do autómato. Se encontro "=", imprimo a soma acumulada até esse ponto. Caso contrário, se o autómato estiver no estado "on", adiciono o número à soma total.


Após processar toda a entrada, verifico se o autómato está num estado de aceitação. Se sim, retorno a soma total e uma mensagem indicando que o token é válido. Se não, retorno uma mensagem de erro, indicando que o autómato não atingiu um estado final.

**Utilização do AFD:**
De forma a usar o automáto começo então por definir os estados, o estado inicial e os estados de aceitação. Em seguida, crio o autómato finito e começo um loop infinito para receber input do utilizador. 

Utilizo uma expressão regular para filtrar apenas os tokens relevantes do input: "=", "on" e "off" (case insensitive), e sequências de dígitos.

Estes tokens são então passados ao método process_input() para serem processados.

Depois de processar o input, imprimo o resultado e reseto o autómato para o estado inicial.
