from collections import deque

def criar_grafo_metro():
    """
    Define as conexões (arestas) da rede de metrô (grafo não direcionado)
    usando lista de adjacência.
    
    Mapa simplificado:
    - A <-> B, A <-> C
    - B <-> A, B <-> D, B <-> E
    - C <-> A, C <-> F
    - D <-> B, D <-> E
    - E <-> B, E <-> D, E <-> F
    - F <-> C, F <-> E
    """
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B', 'E'],
        'E': ['B', 'D', 'F'],
        'F': ['C', 'E']
    }
    return grafo

def bfs(grafo, inicio):
    """
    Implementação da Busca em Largura (BFS).
    Retorna a ordem em que os vértices foram visitados.
    """
    visitados = set()
    fila = deque([inicio])
    visitados.add(inicio)
    
    ordem_visita = []
    
    while fila:
        vertice_atual = fila.popleft()
        ordem_visita.append(vertice_atual)
        
        # Para cada vizinho do vértice atual, se ainda não visitado, adiciona na fila
        for vizinho in grafo[vertice_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                
    return ordem_visita

def dfs_recursivo(grafo, vertice, visitados, ordem_visita):
    """
    Função auxiliar recursiva para DFS.
    """
    visitados.add(vertice)
    ordem_visita.append(vertice)
    
    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            dfs_recursivo(grafo, vizinho, visitados, ordem_visita)

def dfs(grafo, inicio):
    """
    Implementação da Busca em Profundidade (DFS) chamando a função recursiva.
    """
    visitados = set()
    ordem_visita = []
    dfs_recursivo(grafo, inicio, visitados, ordem_visita)
    return ordem_visita

def main():
    # 1) Criar o grafo (lista de adjacência)
    grafo_metro = criar_grafo_metro()
    
    # 2) Executar BFS a partir da Estação A
    ordem_bfs = bfs(grafo_metro, 'A')
    print("Ordem de visita (BFS) a partir de A:", ordem_bfs)
    
    # 3) Executar DFS a partir da Estação A
    ordem_dfs = dfs(grafo_metro, 'A')
    print("Ordem de visita (DFS) a partir de A:", ordem_dfs)
    
    # 4) Discussão sobre as diferenças:
    print("\n--- Comparação BFS vs DFS ---")
    print("1) Qual abordagem percorre as estações primeiro?")
    print("   - A BFS visita todos os vizinhos de A (B e C) antes de aprofundar.")
    print("   - A DFS segue profundamente por um caminho antes de voltar.")
    
    print("\n2) Em qual situação a DFS seria mais útil?")
    print("   - A DFS pode ser útil quando queremos explorar caminhos completos,")
    print("     por exemplo, para detectar ciclos ou quando precisamos de um")
    print("     percurso que desça ao máximo em cada ramificação (ex.: backtracking).")
    
    print("\n3) Em qual situação a BFS seria mais eficiente?")
    print("   - A BFS é melhor para encontrar o caminho mais curto (em termos de")
    print("     número de arestas) entre duas estações. Também é útil quando")
    print("     desejamos processar o grafo em 'camadas' a partir de uma origem.")
    
if __name__ == "__main__":
    main()
