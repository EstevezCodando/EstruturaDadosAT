import math
import time
import sys

# Mapeamento dos bairros para índices
indice = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5
}
rotulo = {v: k for k, v in indice.items()}  # inverso, se precisar exibir

def construir_matriz_adjacencia_6():
    """
    Constrói a matriz de adjacência 6x6 de acordo com a tabela:
      A-B (4 km), A-C (2 km), B-D (5 km), C-D (8 km), C-E (3 km),
      D-F (6 km), E-F (1 km).
    Para BFS, só importa 'existência' de aresta, mas vamos marcar
    com peso=1 e inf para 'sem aresta'.
    """
    n = 6
    matriz = [[math.inf]*n for _ in range(n)]
    
    # Distância pra si mesmo = 0
    for i in range(n):
        matriz[i][i] = 0
    
    # Basta marcar que existe aresta quando a tabela diz que há conexão
    # A->B (4 km) => como BFS não liga para pesos, poderíamos pôr 1. 
    # Aqui farei peso=1 para "existe aresta".
    
    # A (0) - B (1)
    matriz[0][1] = 1
    matriz[1][0] = 1
    
    # A (0) - C (2)
    matriz[0][2] = 1
    matriz[2][0] = 1
    
    # B (1) - D (3)
    matriz[1][3] = 1
    matriz[3][1] = 1
    
    # C (2) - D (3)
    matriz[2][3] = 1
    matriz[3][2] = 1
    
    # C (2) - E (4)
    matriz[2][4] = 1
    matriz[4][2] = 1
    
    # D (3) - F (5)
    matriz[3][5] = 1
    matriz[5][3] = 1
    
    # E (4) - F (5)
    matriz[4][5] = 1
    matriz[5][4] = 1

    return matriz

def construir_lista_adjacencia_6():
    """
    Constrói a lista de adjacência equivalente, baseado na mesma tabela.
    """
    n = 6
    # Inicialmente, cada vértice sem vizinhos
    lista_adj = [[] for _ in range(n)]
    
    # A->B, A->C
    lista_adj[0].append(1)
    lista_adj[1].append(0)
    lista_adj[0].append(2)
    lista_adj[2].append(0)
    
    # B->D
    lista_adj[1].append(3)
    lista_adj[3].append(1)
    
    # C->D, C->E
    lista_adj[2].append(3)
    lista_adj[3].append(2)
    lista_adj[2].append(4)
    lista_adj[4].append(2)
    
    # D->F
    lista_adj[3].append(5)
    lista_adj[5].append(3)
    
    # E->F
    lista_adj[4].append(5)
    lista_adj[5].append(4)
    
    return lista_adj

def bfs_matriz_adjacencia(matriz, vertice_inicial):
    n = len(matriz)
    visitados = [False]*n
    fila = [vertice_inicial]
    visitados[vertice_inicial] = True
    resultado = []

    while fila:
        u = fila.pop(0)
        resultado.append(u)
        for v in range(n):
            # Se houver aresta (matriz[u][v] != inf) e não foi visitado
            if matriz[u][v] != math.inf and not visitados[v]:
                visitados[v] = True
                fila.append(v)
    return resultado

def bfs_lista_adjacencia(lista_adj, vertice_inicial):
    n = len(lista_adj)
    visitados = [False]*n
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

def existe_aresta_matriz(matriz, u, v):
    return (matriz[u][v] != math.inf)

def existe_aresta_lista(lista_adj, u, v):
    return (v in lista_adj[u])

def comparar_representacoes_tabela():
    """
    Constrói a matriz e a lista de adjacência para as 6 estações (A-F),
    executa BFS a partir de A (índice 0) e compara tempos, 
    também testa a existência de aresta para diversos pares.
    """
    print("\n=== COMPARANDO COM A TABELA DE 6 BAIRROS ===")

    # Constrói matriz e lista
    matriz = construir_matriz_adjacencia_6()
    lista_adj = construir_lista_adjacencia_6()

    # 1) Medir tempo de BFS em cada
    vertice_inicial = 0  # A
    t0 = time.time()
    visita_matriz = bfs_matriz_adjacencia(matriz, vertice_inicial)
    t1 = time.time()
    tempo_bfs_matriz = t1 - t0

    t0 = time.time()
    visita_lista = bfs_lista_adjacencia(lista_adj, vertice_inicial)
    t1 = time.time()
    tempo_bfs_lista = t1 - t0

    print("--- BFS ---")
    print(f"BFS na Matriz (inicial=A=0): tempo={tempo_bfs_matriz:.6f}s, ordem visita={visita_matriz}")
    print(f"BFS na Lista  (inicial=A=0): tempo={tempo_bfs_lista:.6f}s, ordem visita={visita_lista}")

    # 2) Verificar aresta em alguns pares
    consultas = [(0,1), (0,5), (2,4), (3,5)]
    print("\n--- Teste de existência de aresta ---")
    for (x, y) in consultas:
        em = existe_aresta_matriz(matriz, x, y)
        el = existe_aresta_lista(lista_adj, x, y)
        print(f"Aresta {rotulo[x]}-{rotulo[y]}? Matriz={em}, Lista={el}")

    # 3) Comparação de uso de memória
    memoria_matriz = sys.getsizeof(matriz) 
    memoria_lista = sys.getsizeof(lista_adj)
    print(f"\n--- Uso de memória (aproximado) ---")
    print(f"Matriz: ~{memoria_matriz} bytes")
    print(f"Lista:  ~{memoria_lista} bytes")

def main():
    # Comparar representações com a Tabela de 6 bairros (A-F)
    comparar_representacoes_tabela()

    # Se quiser, pode continuar chamando os testes de grafos grandes/esparsos/densos
    # Aqui só dou exemplo de "como ficaria" se quisesse reutilizar o código original
    #
    # from exercicio_original import comparar_representacoes
    # comparar_representacoes(qtd_vertices=2000, qtd_arestas=3000, qtd_consultas=10000)
    # comparar_representacoes(qtd_vertices=2000, qtd_arestas=1500000, qtd_consultas=10000)

if __name__ == "__main__":
    main()
