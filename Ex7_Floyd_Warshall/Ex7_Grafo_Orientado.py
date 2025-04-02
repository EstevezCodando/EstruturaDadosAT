import math

def criar_matriz_de_adjacencia():
    """
    Cria e retorna uma matriz de adjacência 6x6 para os bairros A-F,
    de forma DIRECIONADA, baseado na tabela:
      A->B=5, A->C=10,
      B->C=3, B->D=8,
      C->D=2, C->E=7,
      D->E=4, D->F=6,
      E->F=5
    Para fazer um grafo não-direcionado, duplicaríamos cada aresta no sentido inverso.
    
    Índices:
      A -> 0, B -> 1, C -> 2, D -> 3, E -> 4, F -> 5
    """
    INF = math.inf
    n = 6
    # Inicializa tudo com ∞
    matriz = [[INF] * n for _ in range(n)]

    # Distância de um bairro para ele mesmo = 0
    for i in range(n):
        matriz[i][i] = 0

    # Preenche de acordo com a tabela (direcionada):
    # A(0)->B(1)=5
    matriz[0][1] = 5
    # A(0)->C(2)=10
    matriz[0][2] = 10
    # B(1)->C(2)=3
    matriz[1][2] = 3
    # B(1)->D(3)=8
    matriz[1][3] = 8
    # C(2)->D(3)=2
    matriz[2][3] = 2
    # C(2)->E(4)=7
    matriz[2][4] = 7
    # D(3)->E(4)=4
    matriz[3][4] = 4
    # D(3)->F(5)=6
    matriz[3][5] = 6
    # E(4)->F(5)=5
    matriz[4][5] = 5

    return matriz

def floyd_warshall(distancias):
    """
    Implementa o Algoritmo de Floyd-Warshall para atualizar a matriz 'distancias'
    de forma que distancias[i][j] passe a representar a menor distância entre i e j.
    
    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) para k em [0..n-1].
    """
    n = len(distancias)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distancias[i][k] + distancias[k][j] < distancias[i][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
    return distancias

def imprimir_matriz(distancias):
    """
    Imprime a matriz de distâncias de forma organizada.
    """
    n = len(distancias)
    rotulo = ['A','B','C','D','E','F']
    print("Matriz de Menores Distâncias (Floyd-Warshall):\n")

    # Cabeçalho
    print("   ", end="")
    for col in range(n):
        print(f"{rotulo[col]:>4}", end="")
    print()
    
    # Linhas
    for i in range(n):
        print(f"{rotulo[i]} ", end="")
        for j in range(n):
            val = distancias[i][j]
            if val == math.inf:
                print(f"{'inf':>4}", end="")
            else:
                print(f"{val:>4}", end="")
        print()

def main():
    # 1) Criar a matriz de adjacência conforme a tabela
    matriz = criar_matriz_de_adjacencia()

    # 2) Aplicar Floyd-Warshall
    floyd_warshall(matriz)

    # 3) Imprimir a matriz resultante
    imprimir_matriz(matriz)

    # 4) Questões
    #    a) Tempo mínimo de A até F?
    #       A=0, F=5
    distancia_A_F = matriz[0][5]
    print(f"\n1) Distância mínima de A até F: {distancia_A_F if distancia_A_F < math.inf else 'Sem rota'}")

    print("\n2) Se uma rua fosse fechada, poderíamos definir a aresta como inf. "
          "O Floyd-Warshall recalcularia as rotas possíveis ou manteria 'inf' se não houver outro caminho.")

    print("\n3) Planejamento de novas linhas: ver onde as distâncias ainda estão altas ou 'inf' e considerar "
          "novas conexões para encurtar o trajeto, simulando novamente com Floyd-Warshall.")

if __name__ == "__main__":
    main()
