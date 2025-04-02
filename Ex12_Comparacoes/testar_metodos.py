import time

from gerar_distancias import gerar_distancias
from tsp_held_karp import tsp_held_karp
from tsp_vizinho_mais_proximo import tsp_vizinho_mais_proximo
from tsp_forca_bruta import tsp_forca_bruta
from tsp_genetico import tsp_genetico



def testar_metodos(n=6):
    # 1) Gera matriz de distâncias
    dist = gerar_distancias(n, 20)

    print(f"\n=== Comparando métodos para TSP com {n} cidades ===")

    # Força Bruta (se n <= 10, por exemplo)
    if n <= 10:
        t0 = time.time()
        custo_fb, rota_fb = tsp_forca_bruta(dist)
        t1 = time.time()
        print(f"[Força Bruta] custo={custo_fb}, rota={rota_fb}, tempo={t1 - t0:.4f}s")

    # Held-Karp (n <= ~15)
    if n <= 15:
        t0 = time.time()
        custo_hk, rota_hk = tsp_held_karp(dist)
        t1 = time.time()
        print(f"[Held-Karp] custo={custo_hk}, rota={rota_hk}, tempo={t1 - t0:.4f}s")

    # Vizinho mais próximo
    t0 = time.time()
    custo_vm, rota_vm = tsp_vizinho_mais_proximo(dist)
    t1 = time.time()
    print(f"[Vizinho Mais Próximo] custo={custo_vm}, rota={rota_vm}, tempo={t1 - t0:.4f}s")

    # Genético
    t0 = time.time()
    custo_gen, rota_gen = tsp_genetico(dist, tam_pop=50, geracoes=200, taxa_mut=0.1)
    t1 = time.time()
    print(f"[Genético] custo={custo_gen}, rota={rota_gen}, tempo={t1 - t0:.4f}s")
