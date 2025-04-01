from GerenciaRoteador import GerenciadorRoteador

def main():
    roteador = GerenciadorRoteador()

    # Inserindo alguns pacotes de exemplo
    roteador.inserir_pacote(id_pacote=200, prioridade=5, tempo_transmissao=0.2)
    roteador.inserir_pacote(id_pacote=201, prioridade=1, tempo_transmissao=0.5)
    roteador.inserir_pacote(id_pacote=202, prioridade=10, tempo_transmissao=0.1)
    roteador.inserir_pacote(id_pacote=203, prioridade=3, tempo_transmissao=0.3)

    # Visualizando o estado da Heap
    print("\nAntes de qualquer remoção:")
    roteador.visualizar_heap()

    # Remover o pacote de maior prioridade (menor valor)
    print("\nRemovendo pacote prioritário:")
    roteador.remover_pacote_prioritario()

    # Visualiza novamente
    print("\nDepois de remover um pacote:")
    roteador.visualizar_heap()

    # Atualizar a prioridade de um pacote (por exemplo, tornar o 202 mais urgente)
    print("\nAtualizando prioridade do pacote 202 para 0 (mais urgente):")
    roteador.atualizar_prioridade_pacote(202, 0)
    roteador.visualizar_heap()

    # Removendo novamente o de maior prioridade
    print("\nRemovendo pacote prioritário após atualização:")
    roteador.remover_pacote_prioritario()
    roteador.visualizar_heap()

if __name__ == "__main__":
    main()
