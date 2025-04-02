import math
import random

def gerar_rota_aleatoria(n):
    rota = list(range(1, n))  # fixa 0 como primeiro
    random.shuffle(rota)
    return [0] + rota + [0]

def custo_rota(distancias, rota):
    return sum(distancias[rota[i]][rota[i+1]] for i in range(len(rota)-1))

def populacao_inicial(n, tam_pop=50):
    """
    Gera 'tam_pop' rotas aleatórias para n cidades (fixando 0 como origem).
    """
    return [gerar_rota_aleatoria(n) for _ in range(tam_pop)]

def cruzamento_pmx(pai1, pai2):
    """
    Exemplo de cruzamento PMX para TSP (ignorando o fato de termos 0 no início/fim).
    Supõe que pai1[0]=pai2[0]=0 e pai1[-1]=pai2[-1]=0 e não mexe neles.
    """
    n = len(pai1)
    # retiramos a posição 0 e -1 (fixos) para cruzar só o miolo
    slice1 = pai1[1:-1]
    slice2 = pai2[1:-1]
    size = len(slice1)
    filho = [None]*size

    # Ponto de corte
    a, b = sorted([random.randint(0, size-1) for _ in range(2)])
    # Copia a fatia de pai1
    for i in range(a, b+1):
        filho[i] = slice1[i]

    # PMX
    for i in range(a, b+1):
        elem = slice2[i]
        if elem not in filho[a:b+1]:
            pos = i
            # encontra local p/ elem
            while True:
                elem2 = slice1[pos]
                pos2 = slice2.index(elem2)
                if filho[pos2] is None:
                    filho[pos2] = elem
                    break
                pos = pos2

    # Preenche restantes
    for i in range(size):
        if filho[i] is None:
            filho[i] = slice2[i]

    return [0] + filho + [0]

def mutacao(rota, taxa=0.1):
    # Embaralha 2 cidades do miolo com certa probabilidade
    if random.random() < taxa:
        i = random.randint(1, len(rota)-2)
        j = random.randint(1, len(rota)-2)
        rota[i], rota[j] = rota[j], rota[i]

def selecao_roleta(pop, distancias):
    """
    Seleção por roleta: prob(rota) ~ 1/custo_rota.
    """
    custos = [custo_rota(distancias, r) for r in pop]
    aptidoes = [1.0/c for c in custos]  # menor custo => apt mais alta
    soma_apt = sum(aptidoes)
    pick = random.random()*soma_apt
    acum = 0
    for i, ap in enumerate(aptidoes):
        acum += ap
        if acum >= pick:
            return pop[i]
    return pop[-1]

def tsp_genetico(distancias, tam_pop=50, geracoes=100, taxa_mut=0.1):
    """
    Retorna (melhor_custo, melhor_rota) usando algoritmo genético simples.
    """
    n = len(distancias)
    pop = populacao_inicial(n, tam_pop)

    melhor_sol = None
    melhor_custo = math.inf

    for _ in range(geracoes):
        nova_pop = []
        for __ in range(tam_pop//2):
            pai1 = selecao_roleta(pop, distancias)
            pai2 = selecao_roleta(pop, distancias)
            filho1 = cruzamento_pmx(pai1, pai2)
            filho2 = cruzamento_pmx(pai2, pai1)
            mutacao(filho1, taxa_mut)
            mutacao(filho2, taxa_mut)
            nova_pop.append(filho1)
            nova_pop.append(filho2)

        pop = nova_pop

        # verifica melhor
        for r in pop:
            c = custo_rota(distancias, r)
            if c < melhor_custo:
                melhor_custo = c
                melhor_sol = r[:]

    return melhor_custo, melhor_sol
