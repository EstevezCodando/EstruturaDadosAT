import math
from heapq import heappush, heappop

def criar_grafo_bairros():
    """
    Retorna um grafo (dicionário) onde cada chave é um bairro
    e cada valor é uma lista de tuplas (vizinho, distancia).
    Exemplo simplificado:
      CD -> Centro de Distribuição
      A, B, C, D, F -> Bairros
    """
    grafo = {
        'CD': [('A', 2), ('B', 5)],
        'A':  [('CD', 2), ('C', 1), ('D', 7)],
        'B':  [('CD', 5), ('C', 2), ('F', 10)],
        'C':  [('A', 1), ('B', 2), ('F', 6)],
        'D':  [('A', 7), ('F', 3)],
        'F':  [('B', 10), ('C', 6), ('D', 3)]
    }
    return grafo

def dijkstra(grafo, origem, destino):
    """
    Implementa o Algoritmo de Dijkstra para encontrar o menor caminho
    entre 'origem' e 'destino' em um grafo ponderado (não direcionado).
    
    :param grafo: dicionário {no: [(vizinho, peso), ...]}
    :param origem: nó (bairro) de partida
    :param destino: nó (bairro) de destino
    :return: (distancia_minima, caminho) onde
             distancia_minima é a soma dos pesos
             caminho é a lista de nós percorridos
    """
    # Distância acumulada até cada nó (inicia com infinito)
    distancias = {no: math.inf for no in grafo}
    distancias[origem] = 0

    # Para reconstruir o caminho, guardamos quem é o 'pai' de cada nó
    pai = {no: None for no in grafo}

    # Min-heap para escolher o vértice de menor distância acumulada
    heap = []
    heappush(heap, (0, origem))  # (distancia, nó)
    
    # Conjunto ou dicionário para controlar visitados
    visitados = set()

    while heap:
        dist_atual, no_atual = heappop(heap)

        # Se já visitamos este nó, podemos ignorar
        if no_atual in visitados:
            continue
        
        visitados.add(no_atual)

        # Se chegamos ao destino, podemos parar
        if no_atual == destino:
            break

        # Analisa vizinhos do nó atual
        for (vizinho, peso) in grafo[no_atual]:
            nova_dist = dist_atual + peso
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                pai[vizinho] = no_atual
                heappush(heap, (nova_dist, vizinho))

    # Reconstrói o caminho do destino até a origem, usando 'pai'
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = pai[atual]
    caminho.reverse()  # Pois construímos de trás pra frente

    return distancias[destino], caminho

def main():
    # 1) Cria o grafo (bairro e ruas, com distâncias em km)
    grafo = criar_grafo_bairros()

    # 2) Define origem (Centro de Distribuição) e destino
    origem = 'CD'
    destino = 'F'

    # 3) Executa o algoritmo de Dijkstra
    distancia_minima, caminho_otimo = dijkstra(grafo, origem, destino)

    # 4) Exibe resultados
    print(f"Menor rota de {origem} até {destino} encontrada pelo Dijkstra:")
    print(" -> ".join(caminho_otimo))
    print(f"Distância total = {distancia_minima} km")

    # 5) Respostas às perguntas
    print("\n--- Perguntas ---")
    print("1) O algoritmo encontrou exatamente o caminho que você esperava?")
    print("   - Possivelmente sim, se você já tinha uma ideia de qual fosse a rota mais curta.")
    print("     Caso contrário, pode surpreender se havia caminhos com somas de arestas menores do que imaginávamos.")

    print("\n2) Como essa abordagem pode ser usada para otimizar a logística em cidades maiores?")
    print("   - O Dijkstra encontra rotas de custo mínimo em grafos ponderados. Para grandes cidades, podemos armazenar")
    print("     cada bairro como um nó e cada rua como aresta com peso (distância, tempo ou custo), e então aplicamos")
    print("     o Dijkstra (ou variações) para planejar rotas de entrega otimizadas, economizando combustível e tempo.")

    print("\n3) Se os pesos representassem o tempo de viagem em vez de distância, como isso afetaria a solução?")
    print("   - O algoritmo em si permanece o mesmo; a lógica é idêntica. A única diferença é que os pesos das arestas")
    print("     correspondem a tempos (por exemplo, minutos) em vez de quilômetros. Dessa forma, o Dijkstra encontraria")
    print("     a rota de menor duração. Em congestionamentos, poderíamos ajustar o peso para refletir velocidades menores.")

if __name__ == "__main__":
    main()
