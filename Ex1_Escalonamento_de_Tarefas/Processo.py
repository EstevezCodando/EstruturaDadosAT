class Processo:
    def __init__(self, id_processo: int, tempo_execucao: int, prioridade: int):
        """
        Representa um processo do sistema operacional.
        
        :param id_processo: Identificação única do processo
        :param tempo_execucao: Tempo necessário para executar o processo (em unidades de tempo)
        :param prioridade: Prioridade do processo (quanto menor, maior a prioridade)
        """
        self.id_processo = id_processo
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade

    def __repr__(self):
        """
        Retorna uma representação em string do processo,
        útil para depuração e logs.
        """
        return (f"Processo("
                f"id={self.id_processo}, "
                f"tempo={self.tempo_execucao}, "
                f"prioridade={self.prioridade})")
