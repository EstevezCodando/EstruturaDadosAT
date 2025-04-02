
import random


def gerar_distancias(n, max_dist=100):
    """
    Gera uma matriz de distâncias n x n para TSP, simétrica e com valores até max_dist.
    """
    dist = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            d = random.randint(1, max_dist)
            dist[i][j] = d
            dist[j][i] = d
    return dist
