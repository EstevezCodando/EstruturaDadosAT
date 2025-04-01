from Pacotes import Pacote
class HeapMinima:
    def __init__(self):
        """
        Heap Mínima usando um array (lista Python).
        Cada elemento será um objeto Pacote,
        onde menor prioridade = maior urgência.
        """
        self._elementos = []

    def _subir_no_heap(self, indice_filho: int):
        """
        Ajusta o heap de baixo para cima.
        """
        while indice_filho > 0:
            indice_pai = (indice_filho - 1) // 2
            
            # Se o pacote do filho tiver prioridade menor que a do pai, trocar
            if self._elementos[indice_filho].prioridade < self._elementos[indice_pai].prioridade:
                self._elementos[indice_filho], self._elementos[indice_pai] = (
                    self._elementos[indice_pai],
                    self._elementos[indice_filho]
                )
                indice_filho = indice_pai
            else:
                break

    def _descer_no_heap(self, indice_pai: int):
        """
        Ajusta o heap de cima para baixo, após remoção do topo.
        """
        tamanho = len(self._elementos)
        while True:
            indice_esquerda = 2 * indice_pai + 1
            indice_direita = 2 * indice_pai + 2
            indice_menor = indice_pai

            # Verifica se o filho esquerdo existe e se tem prioridade menor
            if (indice_esquerda < tamanho and
                self._elementos[indice_esquerda].prioridade < self._elementos[indice_menor].prioridade):
                indice_menor = indice_esquerda

            # Verifica o direito
            if (indice_direita < tamanho and
                self._elementos[indice_direita].prioridade < self._elementos[indice_menor].prioridade):
                indice_menor = indice_direita

            # Se trocou, precisamos continuar descendo
            if indice_menor != indice_pai:
                self._elementos[indice_pai], self._elementos[indice_menor] = (
                    self._elementos[indice_menor],
                    self._elementos[indice_pai]
                )
                indice_pai = indice_menor
            else:
                break

    def inserir(self, pacote: Pacote):
        """
        Insere um pacote na heap e ajusta a estrutura.
        """
        self._elementos.append(pacote)
        self._subir_no_heap(len(self._elementos) - 1)

    def remover_minimo(self) -> Pacote:
        """
        Remove e retorna o pacote de menor prioridade (maior urgência).
        Retorna None se estiver vazio.
        """
        if not self._elementos:
            return None
        
        # Trocamos topo com o último elemento
        self._elementos[0], self._elementos[-1] = self._elementos[-1], self._elementos[0]
        pacote_removido = self._elementos.pop()  # remove do final da lista

        # Ajusta o heap
        if self._elementos:
            self._descer_no_heap(0)

        return pacote_removido

    def atualizar_prioridade(self, id_pacote: int, nova_prioridade: int):
        """
        Atualiza a prioridade de um pacote pelo seu ID e reordena o heap.
        (Implementação simplificada: O(n) para achar o pacote)
        """
        for indice, pacote in enumerate(self._elementos):
            if pacote.id_pacote == id_pacote:
                pacote.prioridade = nova_prioridade
                # Após atualizar a prioridade, precisamos subir ou descer conforme necessário.
                self._subir_no_heap(indice)
                self._descer_no_heap(indice)
                break

    def __len__(self):
        return len(self._elementos)

    def __str__(self):
        return str(self._elementos)
