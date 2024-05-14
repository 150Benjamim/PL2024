# TP6: Gramática Independente de Contexto

## Autor
- Benjamim Meleiro Rodrigues
- A93323

## Objetivos
Construir uma gramática independente de contexto para uma linguagem simples, que envolve os seguintes casos:

- ?a
- b=a*2/(27-3)
- !a+b
- c=a*b/(a/b)

## Resolução


```
T = {'?', var, '=', '*', int, '/', '(', ')', '-', '!'}

N = {S, exp1, exp2, exp3, opr1, opr2}

S = S


P = {

S -> '?' var             LA = {'?'}
   | var '=' exp1        LA = {var}
   | '!' exp1            LA = {'!'}

exp1 -> exp2 opr1        LA = {'(', var, int}

opr1 -> '+' exp1         LA = {'+'}
      | '-' exp1         LA = {'-'}
      | ε                LA = {')', $}

exp2 -> exp3 opr2        LA = {'(', var, int}

opr2 -> '*' exp1         LA = {'*'}
      | '/' exp1         LA = {'/'}
      | ε                LA = {')', $}

exp3 -> '(' exp1 ')'     LA = {'('}
      | var              LA = {var}
      | int              LA = {int}
      
}

