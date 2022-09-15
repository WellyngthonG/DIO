"""
================================================== ==
Bootcamp Geração Tech Unimed-BH - Ciência de Dados
================================================== ==
2/3 - Cachorros-Quentes
================================================== ==
2012 minutos pelo maior número de dois: Em um novo recorde mundial, a Competição de Cachorros de Nathan, devorou ​​68 cachorros-que aumentou, um incrível aumento em relação aos 62 devorados em relação aos 62 devorados em 11.
O restaurante Nathan's Famous Corporation, localizado no Brooklyn, NY, é o responsável pela competição. eles não são deliciosos quando são famosos cachorros-gostos-gostos, assunto é eles tão bons. Eles devem ser executados no Livro de Registros do compromisso, mas devem cumprir um compromisso de cumprir os fatos da competição. Em particular, eles devem o número médio de cachorros-quentes consumidores informados durante a competição.
Você pode ajudar-los? Eles prometem-lo com um dos seus paisgás cachorros-quentes Dados o número total de cachorros-quentes consumidos e o total de participantes na competição, você deve escrever um programa para determinar o número médio de cachorros-quentes consumidos.
Entrada
Uma linha que consiste em dois números inteiros H e P (1 ≤ H, P ≤ 1000), respectivamente, indicando o número total de cachorros-quentes consumidos e o total de participantes únicos na competição.
Saída
Seu programa deve produzir uma linha única com um número racional representando o número médio de cachorros-que fornecedores pelos participantes. O resultado deve ser escrito como um número racional com dois dígitos após o ponto decimal, dois dígitos necessários.
--------------------------------------------
| Exemplo de Entrada | Exemplo de Saída |
--------------------------------------------
| 10 90 | 0,11 |
--------------------------------------------
| 840 11 | 76,36 |
--------------------------------------------
| 1 50 | 0,02 |
--------------------------------------------
| 34 1000 | 0,03 |
--------------------------------------------1
| 35 1000 | 0,04 |
--------------------------------------------
SOLUÇÃO ABAIXO:
"""
valores = input().split() 
total=int(valores[0])
participantes=int(valores[1])

resultado=total/participantes

print(f"{resultado:2.2f}")