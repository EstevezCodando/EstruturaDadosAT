from Processo import Processo


class HeapProcessos:
    def __init__(self):
        """
        Heap binária para gerenciar processos.
        Internamente armazenamos tuplas do tipo (prioridade, id, tempo_execucao, objeto_processo).
        """
        self._heap = []

    def _subir_no_heap(self, indice_filho: int):
        """
        Ajusta o heap de baixo para cima.
        """
        # Enquanto não chegamos na raiz (índice 0)
        # e a prioridade do filho for menor que a do pai, trocamos.
        while indice_filho > 0:
            indice_pai = (indice_filho - 1) // 2
            
            if self._heap[indice_filho][0] < self._heap[indice_pai][0]:
                self._heap[indice_filho], self._heap[indice_pai] = (
                    self._heap[indice_pai], 
                    self._heap[indice_filho]
                )
                indice_filho = indice_pai
            else:
                break

    def _descer_no_heap(self, indice_pai: int):
        """
        Ajusta o heap de cima para baixo após a remoção do elemento de topo (raiz).
        """
        tamanho = len(self._heap)
        while True:
            indice_esquerda = 2 * indice_pai + 1
            indice_direita = 2 * indice_pai + 2
            indice_menor = indice_pai

            # Verifica se filho esquerdo existe e se é menor
            if (indice_esquerda < tamanho and 
                self._heap[indice_esquerda][0] < self._heap[indice_menor][0]):
                indice_menor = indice_esquerda

            # Verifica se filho direito existe e se é menor
            if (indice_direita < tamanho and 
                self._heap[indice_direita][0] < self._heap[indice_menor][0]):
                indice_menor = indice_direita

            # Se o menor elemento não for o pai, trocamos
            if indice_menor != indice_pai:
                self._heap[indice_pai], self._heap[indice_menor] = (
                    self._heap[indice_menor], 
                    self._heap[indice_pai]
                )
                indice_pai = indice_menor
            else:
                break

    def inserir_processo(self, processo: Processo):
        """
        Insere um novo processo na heap, respeitando a prioridade.
        """
        # Inserimos uma tupla com a prioridade na frente para ordenar corretamente
        registro = (processo.prioridade, processo.id_processo, processo.tempo_execucao, processo)
        self._heap.append(registro)
        self._subir_no_heap(len(self._heap) - 1)

    def remover_melhor_prioridade(self) -> Processo:
        """
        Remove e retorna o processo de maior prioridade (menor número).
        Retorna None se a heap estiver vazia.
        """
        if not self._heap:
            return None
        
        # Troca o primeiro (maior prioridade) com o último
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        _, _, _, processo_removido = self._heap.pop()
        
        # Restaura a propriedade de heap
        if self._heap:
            self._descer_no_heap(0)

        return processo_removido

    def modificar_prioridade(self, id_processo: int, nova_prioridade: int):
        """
        Modifica a prioridade de um processo existente na heap.
        Na prática, precisamos encontrar o processo, mudar sua prioridade
        e reordenar a heap.
        
        Observação: Numa implementação mais robusta, teríamos um dicionário
        auxiliar de ID -> índice da heap para acessar em O(1). 
        Aqui, faremos de forma simplificada (O(n)).
        """
        for indice, (prioridade, pid, tempo, processo) in enumerate(self._heap):
            if pid == id_processo:
                # Atualiza a prioridade do objeto
                processo.prioridade = nova_prioridade
                
                # Atualiza a tupla armazenada na heap
                self._heap[indice] = (nova_prioridade, pid, tempo, processo)
                
                # Precisamos reordenar o heap. Vamos:
                # 1) Subir o nó se necessário
                self._subir_no_heap(indice)
                # 2) Descer o nó se necessário
                self._descer_no_heap(indice)
                return  # Sai após atualizar a primeira ocorrência

    def __len__(self):
        return len(self._heap)

    def __str__(self):
        return str(self._heap)
