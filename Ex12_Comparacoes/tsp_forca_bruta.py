import math
import itertools



def tsp_forca_bruta(distancias):
    """
    Retorna (custo_minimo, melhor_rota) percorrendo todas as permutações.
    Supõe TSP não-direcionado e que queremos voltar à cidade inicial 0.
    """
    n = len(distancias)
    cidades = list(range(1, n))  # fixa cidade 0 como origem
    melhor_custo = math.inf
    melhor_permutacao = None

    for perm in itertools.permutations(cidades):
        # Rota: [0] + perm + [0]
        custo = 0
        atual = 0
        for prox in perm:
            custo += distancias[atual][prox]
            atual = prox
        # voltar à origem
        custo += distancias[atual][0]

        if custo < melhor_custo:
            melhor_custo = custo
            melhor_permutacao = perm

    # Constrói a rota completa
    melhor_rota = [0] + list(melhor_permutacao) + [0]
    return melhor_custo, melhor_rota
