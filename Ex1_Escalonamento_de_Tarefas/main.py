from GerenciadorProcessos import GerenciadorProcessos

if __name__ == "__main__":
    # Cria o gerenciador
    gerenciador = GerenciadorProcessos()

    # Adiciona processos de exemplo
    gerenciador.adicionar_processo(id_processo=101, tempo_execucao=5, prioridade=10)
    gerenciador.adicionar_processo(id_processo=102, tempo_execucao=3, prioridade=1)
    gerenciador.adicionar_processo(id_processo=103, tempo_execucao=2, prioridade=5)
    gerenciador.adicionar_processo(id_processo=104, tempo_execucao=8, prioridade=2)

    # Visualiza o estado atual da heap
    print("\nEstado atual da Heap:")
    gerenciador.visualizar_heap()

    # Executa processo de maior prioridade
    print("\nExecutando o processo de maior prioridade:")
    gerenciador.executar_proximo_processo()

    # Altera prioridade de um processo existente
    print("\nAlterando prioridade do processo 103 para 0 (alta prioridade):")
    gerenciador.alterar_prioridade(103, 0)

    # Visualiza o estado após alteração
    print("\nEstado da Heap após alteração de prioridade:")
    gerenciador.visualizar_heap()

    # Executa o próximo processo (agora o 103 deve ser o primeiro por ter prioridade 0)
    print("\nExecutando o processo de maior prioridade após alteração:")
    gerenciador.executar_proximo_processo()

    # Visualiza o estado final
    print("\nEstado final da Heap:")
    gerenciador.visualizar_heap()
