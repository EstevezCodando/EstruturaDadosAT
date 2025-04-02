import math


def tsp_vizinho_mais_proximo(distancias):
    """
    Retorna (custo, rota) usando a heurística de vizinho mais próximo
    iniciando na cidade 0 e retornando a 0 no final.
    """
    n = len(distancias)
    visitados = [False]*n
    rota = [0]
    visitados[0] = True
    custo_total = 0
    atual = 0

    for _ in range(n-1):
        melhor_dist = math.inf
        proxima_cidade = -1
        for j in range(n):
            if not visitados[j]:
                dist = distancias[atual][j]
                if dist < melhor_dist:
                    melhor_dist = dist
                    proxima_cidade = j
        custo_total += melhor_dist
        rota.append(proxima_cidade)
        visitados[proxima_cidade] = True
        atual = proxima_cidade

    # retorno à cidade 0
    custo_total += distancias[atual][0]
    rota.append(0)
    return custo_total, rota
