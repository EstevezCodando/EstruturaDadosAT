import math
from heapq import heappush, heappop

def criar_grafo_bairros():
    """
    Retorna um grafo (dicionário) onde cada chave é um bairro
    e cada valor é uma lista de tuplas (vizinho, distancia).
    
    Aqui, interpretamos a tabela como 'De -> Para' em um grafo DIRECIONADO.
    """
    grafo = {
        'CD': [('A', 4), ('B', 2)],  # CD->A=4, CD->B=2
        'A':  [('C', 5), ('D', 10)], # A->C=5, A->D=10
        'B':  [('A', 3), ('D', 8)],  # B->A=3, B->D=8
        'C':  [('D', 2), ('E', 4)],  # C->D=2, C->E=4
        'D':  [('E', 6), ('F', 5)],  # D->E=6, D->F=5
        'E':  [('F', 3)],           # E->F=3
        'F':  []                    # F não tem saída listada
    }
    return grafo

def dijkstra(grafo, origem, destino):
    """
    Algoritmo de Dijkstra para grafo direcionado ou não-direcionado.
    (Se for não-direcionado, cada aresta deve aparecer nos dois sentidos.)
    :param grafo: {no: [(vizinho, peso), ...]}
    :param origem: nó (bairro) de partida
    :param destino: nó (bairro) de destino
    :return: (distancia_minima, caminho)
    """
    # Inicializa distâncias com infinito, exceto a origem = 0
    distancias = {no: math.inf for no in grafo}
    distancias[origem] = 0

    # 'pai' serve para reconstruir o caminho
    pai = {no: None for no in grafo}

    # Min-heap para sempre extrair o vértice com menor distância atual
    heap = []
    heappush(heap, (0, origem))
    
    visitados = set()

    while heap:
        dist_atual, no_atual = heappop(heap)

        if no_atual in visitados:
            continue
        
        visitados.add(no_atual)

        # Se chegamos no destino, podemos encerrar
        if no_atual == destino:
            break

        # Explora os vizinhos do nó atual
        for (vizinho, peso) in grafo[no_atual]:
            nova_dist = dist_atual + peso
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                pai[vizinho] = no_atual
                heappush(heap, (nova_dist, vizinho))

    # Reconstruir o caminho do destino até a origem
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = pai[atual]
    caminho.reverse()  # pois adicionamos de trás pra frente

    return distancias[destino], caminho

def main():
    # 1) Cria o grafo baseado na nova tabela (direcionado)
    grafo = criar_grafo_bairros()

    # 2) Definimos a origem (CD) e destino (F)
    origem = 'CD'
    destino = 'F'

    # 3) Executa Dijkstra
    distancia_minima, caminho_otimo = dijkstra(grafo, origem, destino)

    # 4) Exibe resultado
    print(f"Menor rota de {origem} até {destino} encontrada pelo Dijkstra:")
    print(" -> ".join(caminho_otimo) if caminho_otimo[0] == origem else "Não há caminho!")
    print(f"Distância total = {distancia_minima} km" if distancia_minima < math.inf else "Não foi possível chegar.")

    # 5) Perguntas
    print("\n--- Perguntas ---")
    print("1) O algoritmo encontrou o caminho esperado?")
    print("   - Depende de haver realmente uma rota de 'CD' a 'F' usando as conexões diretas definidas.")
    print("2) Uso em cidades maiores?")
    print("   - Pode ser ampliado para quaisquer bairros e ruas, armazenando em um dicionário e usando pesos.")
    print("3) Se os pesos fossem tempo, mudaria algo?")
    print("   - O Dijkstra funcionaria da mesma forma; os pesos passariam a representar minutos ou horas.")

if __name__ == "__main__":
    main()
