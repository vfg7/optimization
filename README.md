Problema da tentativa de otimização do TSP

O caso
O caso foi o retirado da página:http://www.math.uwaterloo.ca/tsp/world/countries.html

Os desafios do caso:

* O TSP (traveling salesperson problem) é um algoritmo famoso conhecido por sua complexidade fazendo com que sua otimização, por si só, já seja um desafio. (Pra mais infos: https://en.wikipedia.org/wiki/Travelling_salesman_problem)

* Para tentar contornar a complexidade do TSP, foi usado o caso de menor tamanho, o exemplo do Saara Ocidental, cujo mapeamento consta apenas 29 cidades.

O algoritmo de otimização utilizado foi o algoritmo da têmpera simulada (simulated annealing). A calibração do algoritmo envolveu:
* estudar os dados do problema e escolher valores da temperatura para garantir uma função de resfriamento compatível com comportamento do problema
* já é sabido que percorrer todas as combinações até achar o caminho mais curto vai levar tempo exponencial. Então, para tentar melhorar as chances do algoritmo acertar o caminho ótimo, foi adicionado um fator para tentar gerar escolhas aleatórias (não-determinísticas)


Documentação
O projeto foi feito em Python, versão 3.7.0

Foram usadas as bibliotecas:

* math
* random

O projeto foi feito no pycharm, então, clonar este repositório e abrir como um novo projeto na referida IDE deve ser o bastante para sua reprodução

Próximos passos

* Por mais que esteja comentado, reconheço que o código precisa de uma refatoração, seja para reescrever alguns métodos de forma mais sucinta, seja para ajudar na legibilidade do código

* Muitas funções foram implementadas do zero e não busquei bibliotecas para o problema, deixando o código em baixo nível. Enquanto considero que há notáveis vantagens em implementar seu código, também reconheço que o uso de bibliotecas e funções pode facilitar a resolução do problema.
