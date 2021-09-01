import math
import random

def mapmaker(i, j):
    #i linhas , j colunas cria e incializa uma matriz com 0 em todos os elementos
    M = []
    for x in range(i):
        A = []
        for y in range(j):
                A.append(0)

        M.append(A)

    # print(M)
    return M

def multilineinput():
    #metodo para entrar várias linhas - cortesia do stackoverflow
    try:
        while True:
            data = input()
            if not data: break
            yield data
    except KeyboardInterrupt:
        return

def distanceMatrix(M=[]):

    N =[]

    for a in range(len(M[0])):
        O = []
        for b in range(len(M[0])):
            if b == a:
                O.append(0)
            else:
                O.append(math.sqrt(pow((float(M[0][a])-float(M[0][b])),2) + pow((float(M[1][a])-float(M[1][b])),2)))

        N.append(O)

    return N

def trivial(n):
    #cria vetor enumerado
    a = []
    for x in range(n):
        a.append(x)

    return a

def costCalculate(sol=[], dist=[]):
    #método passa pelo vetor, calculando a distancia de um ponto a outro em ordem e, por ultimo, do ponto final ao primeiro
    cost = 0
    for x in range(len(sol)):
        # print(cost, " at: ", x)
        if x == len(sol)-1:
            # print(dist[sol[x]][sol[0]])
            cost = cost + dist[sol[x]][sol[0]]
        else:
            cost = cost + dist[sol[x]][sol[x+1]]
            # print(dist[sol[x]][sol[x+1]])

    return cost

def Tempera(pointIndex, t, sol=[], dist=[]):
    #a solução ótima adiciona o ponto atual. O próximo ponto
    s=[]
    nextPoint = 0

    #s é um slice da matriz de solução inicial, sempre tirando os pontos já escolhidos previamente pra evitar repetição
    #nextpoint é, a priori, o próximo ponto na matriz de solução inicial. Caso seja o último ponto, nextpoint é o primeiro ponto pra fechar o ciclo do TSP

    # print("---- temperaure control -----")
    # print("sol so far: ", sol, " and \n index ", pointIndex)
    if pointIndex == len(sol) - 2:
        return
        # print("solution clause 1")
        # epochs = epochs -1
        # if epochs == 0:
        #     return sol
        # else:

    else:
        s = sol[pointIndex + 2:]
        nextPoint = sol[pointIndex + 1]

    keepGoing = True
    newPoint = False

    while keepGoing:
        #seleciona um numero aleatorio e checa a diferença de caminhos
        # print("Select from: ", s)
        n = random.randint(0, len(s) - 1)
        point2check = s[n]
        standard_distance = dist[sol[pointIndex]][nextPoint]
        checkDistance = dist[sol[pointIndex]][point2check] - standard_distance
        # print("Standard: point: city:", sol[pointIndex], " to index:", nextPoint)
        # print("choose: index ", n, " to city: ", point2check, ". check if: ", dist[sol[pointIndex]][point2check], "</>", dist[sol[pointIndex]][nextPoint])

        if checkDistance < 0:
            #go through optimal path
            nextPoint = point2check
            newPoint = True
            keepGoing = False
            #a temperatura vai ser linearmente decrescente 1/(tamanho dos elementos) por chamada do programa, indo de 1 a 0
            # print("\n accepted optimal")

        else:
            if checkDistance == 0:
                #se tiver algum caso que caia nessa coincidencia vou tratar como coin flip
                energy = 0.5

            elif checkDistance > 0:
                #avalia o caminho subótimo

                threshold = math.exp((-1*checkDistance)/(temperature*t))

            choose = random.random()
            # print("will it accept suboptimal? E:", energy, "> C:" ,choose, "?")
            if choose < threshold:
                #suboptimal path
                # print("\n suboptimal true E/C: ",energy,"/",choose, ", T: ", t)
                nextPoint = point2check
                newPoint = True
                keepGoing = False



        s.pop(n) #evitar loops infinitos na escolha do ponto
        if len(s) == 0:
            keepGoing = False

    if newPoint:
        # print("new point!")
        a, b = sol.index(nextPoint), pointIndex + 1
        sol[a], sol[b] = sol[b], sol[a]
    # else:
    #print("good guess: no new point")
    #
    # print("partial sol: ", sol, "\n", "index: ", pointIndex, "points: ", sol[pointIndex], " -> ", nextPoint, " at T:", t)
    # print("next: ", sol.index((nextPoint)))

    if t == 0:
        # print("sol clause 2")
        return sol
    else:
        t = t * alpha * (1 - (1 / len(sol)))
        Tempera(sol.index(nextPoint),t, sol, dist)

    return sol

#---------- let's go --------------
cities =[]
a = list(multilineinput())
# print(a)
cities.append(a) #coordenada x
b = list(multilineinput())
# print(b)
cities.append(b) #coordenada y

distances = distanceMatrix(cities)
scale = len(distances)
# print(distances)
# print(len(distances))
# print(distances[0])

#solução inicial vai ser os pontos em ordem de 1 até n, em que n vai ser o número de cidades.
sol = trivial(scale) #solução inicial
cost = costCalculate(sol, distances)
print("initial estimate: ", sol,"\n",cost)

# for x in range(10):
#     random.shuffle(sol)
#     cost = costCalculate(sol, distances)
#     print("estimate ",x, ": ", sol,"\n",cost)

start_sol = sol[:]
point = 0
temperature = 1000 #temperatura inicial
t = 1 #parametro para resfriamento
alpha = 0.5
running = True
loops = 100000
hey = input("press enter")
optimal = [sol]

print("START: ", start_sol, "\n OPTIMAL: ", optimal[0])

while running:

    a = random.randint(0, len(start_sol)-1)
    # print("START: ", a, "\n ", start_sol)
    start_sol = optimal[-1][:] #sempre usar o último melhor
    start_sol[0], start_sol[a] = start_sol[a], start_sol[0]
    # print("SWAP: ", start_sol, "\n OPTIMAL: ", optimal[0])

    Tempera(point, t, start_sol, distances)
    newCost = costCalculate(start_sol, distances)

    if newCost < cost:
        print(start_sol,"at ", loops, "\n", cost, "/ ", newCost)
        cost = newCost
        optimal.pop()
        opt = start_sol[:]
        optimal.append(opt)


    loops = loops -1
    t = 1
    alpha = random.random() #muda o multiplicador de forma aleatória para gerar diferentes funções de resfriamento

    # if cost == newCost or loops == 0:
    if loops == 0:
        check = input("reiterar?: s/n ")

        if check == 'n':
            running = False
        else:
            if loops == 0:
                l = input("loops? ")
                loops =int(l)
