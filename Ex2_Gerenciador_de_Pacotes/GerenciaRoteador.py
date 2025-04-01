from Pacotes import Pacote
from HeapMin import HeapMinima


class GerenciadorRoteador:
    def __init__(self):
        self.heap_minima = HeapMinima()

    def inserir_pacote(self, id_pacote: int, prioridade: int, tempo_transmissao: float):
        novo_pacote = Pacote(id_pacote, prioridade, tempo_transmissao)
        self.heap_minima.inserir(novo_pacote)
        print(f"Pacote {id_pacote} inserido (prioridade={prioridade}).")

    def remover_pacote_prioritario(self):
        pacote = self.heap_minima.remover_minimo()
        if pacote:
            print(f"Removendo Pacote {pacote.id_pacote} (prioridade={pacote.prioridade}).")
        else:
            print("Não há pacotes na fila.")
        return pacote

    def atualizar_prioridade_pacote(self, id_pacote: int, nova_prioridade: int):
        self.heap_minima.atualizar_prioridade(id_pacote, nova_prioridade)
        print(f"Prioridade do Pacote {id_pacote} atualizada para {nova_prioridade}.")

    def visualizar_heap(self):
        print("Estado atual da Heap (min-heap):")
        print(self.heap_minima)
