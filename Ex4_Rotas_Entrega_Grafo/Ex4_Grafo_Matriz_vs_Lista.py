import time
import random
import sys
import math

def gerar_grafo_aleatorio(qtd_vertices, qtd_arestas):
    """
    Gera um conjunto de arestas aleatórias (sem repetição) para um grafo não direcionado.
    Retorna uma lista de tuplas (u, v).
    """
    # Garante que não gere mais arestas que o máximo possível (grafo simples)
    max_arestas = qtd_vertices * (qtd_vertices - 1) // 2
    if qtd_arestas > max_arestas:
        qtd_arestas = max_arestas

    arestas_possiveis = []
    for u in range(qtd_vertices):
        for v in range(u + 1, qtd_vertices):
            arestas_possiveis.append((u, v))

    # Embaralha e pega as primeiras qtd_arestas
    random.shuffle(arestas_possiveis)
    arestas_selecionadas = arestas_possiveis[:qtd_arestas]

    return arestas_selecionadas

# -----------------------------------------------------------------------------
# 1) Matriz de Adjacência
# -----------------------------------------------------------------------------
def construir_matriz_adjacencia(qtd_vertices, lista_arestas):
    matriz = [[math.inf]*qtd_vertices for _ in range(qtd_vertices)]
    for i in range(qtd_vertices):
        matriz[i][i] = 0

    for (u, v) in lista_arestas:
        # Vamos atribuir peso 1 a todas as arestas para simplificar
        matriz[u][v] = 1
        matriz[v][u] = 1
    return matriz

def bfs_matriz_adjacencia(matriz, vertice_inicial):
    qtd_vertices = len(matriz)
    visitados = [False]*qtd_vertices
    fila = [vertice_inicial]
    visitados[vertice_inicial] = True
    resultado = []

    while fila:
        u = fila.pop(0)
        resultado.append(u)
        # Verifica todos os outros vértices
        for v in range(qtd_vertices):
            # Se houver aresta (matriz[u][v] != inf) e não visitado
            if matriz[u][v] != math.inf and not visitados[v]:
                visitados[v] = True
                fila.append(v)
    return resultado

def existe_aresta_matriz(matriz, u, v):
    """
    Retorna True se existir aresta (peso != inf), False caso contrário.
    """
    return (matriz[u][v] != math.inf)

# -----------------------------------------------------------------------------
# 2) Lista de Adjacência
# -----------------------------------------------------------------------------
def construir_lista_adjacencia(qtd_vertices, lista_arestas):
    lista_adj = [[] for _ in range(qtd_vertices)]
    for (u, v) in lista_arestas:
        lista_adj[u].append(v)
        lista_adj[v].append(u)
    return lista_adj

def bfs_lista_adjacencia(lista_adj, vertice_inicial):
    qtd_vertices = len(lista_adj)
    visitados = [False]*qtd_vertices
    fila = [vertice_inicial]
    visitados[vertice_inicial] = True
    resultado = []

    while fila:
        u = fila.pop(0)
        resultado.append(u)
        for v in lista_adj[u]:
            if not visitados[v]:
                visitados[v] = True
                fila.append(v)
    return resultado

def existe_aresta_lista(lista_adj, u, v):
    """
    Retorna True se v está na lista de adjacência de u, False caso contrário.
    """
    return v in lista_adj[u]

# -----------------------------------------------------------------------------
# 3) Função de teste/comparação
# -----------------------------------------------------------------------------
def comparar_representacoes(qtd_vertices, qtd_arestas, qtd_consultas=1000):
    """
    - Gera um grafo aleatório com qtd_vertices e qtd_arestas.
    - Constrói Matriz e Lista de Adjacência, medindo tempo e memória.
    - Executa BFS, medindo tempo.
    - Verifica existência de aresta entre pares aleatórios, medindo tempo.
    """
    print(f"\n=== COMPARANDO GRAFO ALEATÓRIO ===")
    print(f"Vértices: {qtd_vertices}, Arestas: {qtd_arestas}\n")

    # 1) Gera as arestas
    t0 = time.time()
    lista_arestas = gerar_grafo_aleatorio(qtd_vertices, qtd_arestas)
    t1 = time.time()
    print(f"[Geração das arestas] Tempo: {t1 - t0:.6f} s")

    # 2) Constrói Matriz de Adjacência
    t0 = time.time()
    matriz = construir_matriz_adjacencia(qtd_vertices, lista_arestas)
    t1 = time.time()
    tempo_construcao_matriz = t1 - t0
    memoria_matriz = sys.getsizeof(matriz)  # Aproximação (não soma aninhada)

    # 3) Constrói Lista de Adjacência
    t0 = time.time()
    lista_adj = construir_lista_adjacencia(qtd_vertices, lista_arestas)
    t1 = time.time()
    tempo_construcao_lista = t1 - t0
    memoria_lista = sys.getsizeof(lista_adj)  # Aproximação

    print("--- Construção ---")
    print(f"Matriz de Adjacência: tempo={tempo_construcao_matriz:.6f}s, memória~{memoria_matriz} bytes")
    print(f"Lista de Adjacência:  tempo={tempo_construcao_lista:.6f}s, memória~{memoria_lista} bytes")

    # 4) BFS em cada representação (a partir de um vértice aleatório)
    vertice_inicial = random.randint(0, qtd_vertices - 1)
    t0 = time.time()
    _ = bfs_matriz_adjacencia(matriz, vertice_inicial)
    t1 = time.time()
    tempo_bfs_matriz = t1 - t0

    t0 = time.time()
    _ = bfs_lista_adjacencia(lista_adj, vertice_inicial)
    t1 = time.time()
    tempo_bfs_lista = t1 - t0

    print("--- BFS ---")
    print(f"Matriz: BFS (inicial={vertice_inicial}) -> {tempo_bfs_matriz:.6f}s")
    print(f"Lista:  BFS (inicial={vertice_inicial}) -> {tempo_bfs_lista:.6f}s")

    # 5) Verificação da existência de aresta em pares aleatórios
    consultas = []
    for _ in range(qtd_consultas):
        x = random.randint(0, qtd_vertices - 1)
        y = random.randint(0, qtd_vertices - 1)
        consultas.append((x, y))

    t0 = time.time()
    for (x, y) in consultas:
        existe_aresta_matriz(matriz, x, y)
    t1 = time.time()
    tempo_existe_matriz = t1 - t0

    t0 = time.time()
    for (x, y) in consultas:
        existe_aresta_lista(lista_adj, x, y)
    t1 = time.time()
    tempo_existe_lista = t1 - t0

    print(f"--- {qtd_consultas} consultas de existência de aresta ---")
    print(f"Matriz: {tempo_existe_matriz:.6f}s")
    print(f"Lista:  {tempo_existe_lista:.6f}s")

# -----------------------------------------------------------------------------
# 4) Executando
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Teste 1: Grafo pequeno (6 vértices, 7 arestas)
    comparar_representacoes(qtd_vertices=6, qtd_arestas=7, qtd_consultas=1000)

    # Teste 2: Grafo maior e mais "esparso"
    comparar_representacoes(qtd_vertices=2000, qtd_arestas=3000, qtd_consultas=10000)

    # Teste 3: Grafo maior e "denso" (perto do máximo de arestas)
    # Máximo de arestas (não direcionado) ~ V*(V-1)/2 = 2000*1999/2 = 1.999.000
    # Vamos usar algo menor, mas ainda grande, p/ não demorar tanto
    comparar_representacoes(qtd_vertices=2000, qtd_arestas=1500000, qtd_consultas=10000)
