import math

def criar_matriz_de_adjacencia():
    """
    Cria e retorna uma matriz de adjacência 6x6 para os bairros A-F, 
    com tempos (em minutos). Se não houver conexão direta, usamos math.inf.
    
    Índices:
      A -> 0, B -> 1, C -> 2, D -> 3, E -> 4, F -> 5
    
    Exemplo hipotético de conexões:
      A-B = 10 min, A-C = 15, B-D = 12, C-D = 5,
      D-E = 2, E-F = 8, C-F = 20, ...
    """
    INF = math.inf
    n = 6  # A, B, C, D, E, F
    matriz = [[INF] * n for _ in range(n)]

    # Distância de um bairro para ele mesmo = 0
    for i in range(n):
        matriz[i][i] = 0

    # Preenche algumas conexões diretas (exemplo):
    # A (0) - B (1) = 10
    matriz[0][1] = 10
    matriz[1][0] = 10

    # A (0) - C (2) = 15
    matriz[0][2] = 15
    matriz[2][0] = 15

    # B (1) - D (3) = 12
    matriz[1][3] = 12
    matriz[3][1] = 12

    # C (2) - D (3) = 5
    matriz[2][3] = 5
    matriz[3][2] = 5

    # D (3) - E (4) = 2
    matriz[3][4] = 2
    matriz[4][3] = 2

    # E (4) - F (5) = 8
    matriz[4][5] = 8
    matriz[5][4] = 8

    # C (2) - F (5) = 20
    matriz[2][5] = 20
    matriz[5][2] = 20

    return matriz

def floyd_warshall(distancias):
    """
    Implementa o Algoritmo de Floyd-Warshall para atualizar a matriz 'distancias'
    de forma que distancias[i][j] passe a representar a menor distância (tempo)
    entre i e j (todos os pares).
    
    :param distancias: matriz de adjacência NxN, distancias[i][j] = peso da aresta (i->j)
    :return: matriz distancias (modificada) com os menores tempos
    """
    n = len(distancias)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Se passar por k reduz a distância entre i e j, atualiza
                if distancias[i][k] + distancias[k][j] < distancias[i][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
    return distancias

def imprimir_matriz(distancias):
    """
    Imprime a matriz de distâncias de forma organizada.
    """
    n = len(distancias)
    rotulo = ['A','B','C','D','E','F']  # Ajustar se tiver mais/menos bairros
    print("Matriz de Menores Tempos (após Floyd-Warshall):\n")
    
    # Cabeçalho de colunas
    print("   ", end="")
    for col in range(n):
        print(f"{rotulo[col]:>4}", end="")
    print()
    
    for i in range(n):
        print(f"{rotulo[i]} ", end="")  # Nome da linha
        for j in range(n):
            if distancias[i][j] == math.inf:
                print(f"{'inf':>4}", end="")
            else:
                print(f"{distancias[i][j]:>4}", end="")
        print()

def main():
    # 1) Criar a matriz de adjacência com tempos (em minutos)
    matriz = criar_matriz_de_adjacencia()

    # 2) Aplicar Floyd-Warshall para obter a menor distância entre todos os pares
    floyd_warshall(matriz)

    # 3) Imprimir a matriz resultante
    imprimir_matriz(matriz)

    # 4) Perguntas do Desafio
    #    a) Qual o tempo mínimo para viajar do Bairro A até o Bairro F?
    #       A = 0, F = 5 no nosso mapeamento
    tempo_A_F = matriz[0][5]
    
    print(f"\n1) Tempo mínimo para viajar do Bairro A até o Bairro F: {tempo_A_F} minutos")
    
    print("\n2) Se uma rua entre dois bairros fosse fechada para obras, como isso afetaria a matriz?")
    print("   - Se uma conexão direta (arestas i-j) ficar indisponível, podemos ajustar distancias[i][j] e distancias[j][i] = inf.")
    print("     O Floyd-Warshall recalcularia as rotas considerando caminhos alternativos (se existirem). Se não existir caminho,")
    print("     a distância permaneceria inf, indicando que não há rota possível.")

    print("\n3) Como esse método pode ajudar no planejamento de novas linhas de transporte?")
    print("   - O Floyd-Warshall dá a menor distância entre todos os pares de bairros. Com isso, os planejadores podem identificar")
    print("     os trajetos mais usados, os pontos mais centrais e onde novas linhas podem encurtar viagens longas ou desconectadas.")
    print("     Também permite simular o impacto de adicionar (ou remover) linhas na malha de transporte e recalcular as distâncias.")

if __name__ == "__main__":
    main()
