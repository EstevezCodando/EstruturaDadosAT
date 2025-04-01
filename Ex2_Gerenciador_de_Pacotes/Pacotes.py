class Pacote:
    def __init__(self, id_pacote: int, prioridade: int, tempo_transmissao: float):
        """
        Representa um pacote de rede.
        
        :param id_pacote: Identificador único do pacote
        :param prioridade: Prioridade do pacote (quanto menor, maior a urgência)
        :param tempo_transmissao: Tempo estimado de transmissão do pacote
        """
        self.id_pacote = id_pacote
        self.prioridade = prioridade
        self.tempo_transmissao = tempo_transmissao

    def __repr__(self):
        """
        Retorna uma representação em string do pacote, útil para depuração e logs.
        """
        return (f"Pacote("
                f"id={self.id_pacote}, "
                f"prioridade={self.prioridade}, "
                f"tempo={self.tempo_transmissao})")
