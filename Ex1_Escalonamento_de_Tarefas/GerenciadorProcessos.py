from Processo import Processo
from HeapProcessos import HeapProcessos


class GerenciadorProcessos:
    def __init__(self):
        self.heap_processos = HeapProcessos()

    def adicionar_processo(self, id_processo: int, tempo_execucao: int, prioridade: int):
        """
        Adiciona um novo processo ao gerenciador (heap).
        """
        novo_processo = Processo(id_processo, tempo_execucao, prioridade)
        self.heap_processos.inserir_processo(novo_processo)
        print(f"Processo {id_processo} adicionado com prioridade {prioridade}.")

    def executar_proximo_processo(self):
        """
        Executa (remove da fila) o processo de maior prioridade e retorna seu objeto.
        Se não houver processo, retorna None.
        """
        processo = self.heap_processos.remover_melhor_prioridade()
        if processo:
            print(f"Executando processo {processo.id_processo} (Prioridade {processo.prioridade}).")
        else:
            print("Nenhum processo para executar.")
        return processo

    def alterar_prioridade(self, id_processo: int, nova_prioridade: int):
        """
        Modifica a prioridade de um processo existente.
        """
        self.heap_processos.modificar_prioridade(id_processo, nova_prioridade)
        print(f"Prioridade do processo {id_processo} foi alterada para {nova_prioridade}.")

    def visualizar_heap(self):
        """
        Exibe o estado atual da heap de processos (apenas para depuração).
        """
        print(self.heap_processos)
