import math


def tsp_held_karp(distancias):
    """
    Retorna (custo_minimo, rota) resolvendo TSP via programação dinâmica (Held-Karp).
    """
    n = len(distancias)
    # Tamanho 2^n
    ALL = 1 << n

    # dp[mask][i] = custo mínimo para percorrer o subconjunto de cidades em 'mask'
    #               terminando na cidade i
    dp = [[math.inf]*n for _ in range(ALL)]
    # predecessor para reconstruir rota
    parent = [[-1]*n for _ in range(ALL)]

    # Cidade inicial é 0 => estado base dp[1<<0][0] = 0
    dp[1][0] = 0

    for mask in range(1, ALL):
        for i in range(n):
            if dp[mask][i] == math.inf:
                continue
            # se i não está no subset mask, não prosseguir
            if not (mask & (1 << i)):
                continue
            # tenta ir de i a j
            for j in range(n):
                # se j não pertence a mask
                if mask & (1 << j):
                    continue
                nxt_mask = mask | (1 << j)
                cost = dp[mask][i] + distancias[i][j]
                if cost < dp[nxt_mask][j]:
                    dp[nxt_mask][j] = cost
                    parent[nxt_mask][j] = i

    # Fecha o ciclo voltando à 0
    # min de dp[ALL-1][i] + dist[i][0] para i em [1..n-1]
    fim_mask = (1 << n) - 1
    melhor_custo = math.inf
    ultimo = -1
    for i in range(1, n):
        cost = dp[fim_mask][i] + distancias[i][0]
        if cost < melhor_custo:
            melhor_custo = cost
            ultimo = i

    # Reconstruir rota
    rota = []
    mask = fim_mask
    cidade = ultimo
    while cidade != -1:
        rota.append(cidade)
        temp = parent[mask][cidade]
        mask = mask & ~(1 << cidade)
        cidade = temp
    rota.append(0)
    rota.reverse()

    return melhor_custo, rota
