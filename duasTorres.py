"""
================================================== ==
Bootcamp Geração Tech Unimed-BH - Ciência de Dados
================================================== ==
1/3 - As Duas Torres
================================================== ==
Saruman, o Branco, um grande mago da Terra-média, traiu os bons costumes e se filiou ao lorde do mal, Sauron. Sauron comanda a torre de Minas Morgul, que abriga um dos seus mais temidos servos, o Rei Bruxo de Angmar, um dos Nazgûl (antigos reis humanos que foram corrompidos pelos poderes dos parentes de Sauron). Saruman ou comanda a torre de Orthanc, onde cria seus servos Uruk, mais conveniente que os convencional. Para comunicação, eles usam como relíquias esféricas chamadas Palantír, que não ficam no topo de suas torres.
A Terra-média avança cada vez mais em tecnologia, muito impulsionada pelas guerras que a acometem diariamente. Um dos problemas que tem atrapalhado sua população é a Interferência de Comunicação Mágica (ICM). Os dois pares de Minas Tirith, grande cidadela de Gondo, concluíram que para calcular o ICM para Palantír's, basta dividir a distância entre os os mesmos, pela soma dos diâmetros. Gandalf, o Cinza, chegou a questionar essa conclusão, alegando que ela fazia muito sentido, mas ele não concluiu que dar sentido às coisas não sentido.
Saruman e Sauron precisam de uma comunicação estável, pois seus amigos têm medo de atrapalhar seus planos, portanto, querem saber de ICM há na comunicação de seus planos, para que saibam de magia quanto a empregar na comunicação.
Entrada
A entrada é composta por 3 inteiros, N(0 < N < 10000), X e Y(0 < X, Y < 100), que indicam, respectivamente, a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro Palantír de Saruman.
Saída
Um valor real indicando o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 decimais.
--------------------------------------------
| Exemplo de Entrada | Exemplo de Saída |
--------------------------------------------
| 100 2 2 | 25h00 |
--------------------------------------------
| 200 3 8 | 18.18 |
--------------------------------------------
SOLUÇÃO ABAIXO:
"""
entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

soma=(diametro1+diametro2)
resultado=distancia/soma
print(f"{resultado:2.2f}")