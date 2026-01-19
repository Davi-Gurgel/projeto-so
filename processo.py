class Processo:
    
    def __init__(self, pid, tempo_chegada, duracao):
        self.pid = pid
        self.tempo_chegada = tempo_chegada
        self.duracao = duracao
        self.tempo_restante = duracao
        self.tempo_inicio = None
        self.tempo_fim = None
    
    def tempo_retorno(self):
        return self.tempo_fim - self.tempo_chegada if self.tempo_fim else 0
    
    def tempo_resposta(self):
        return self.tempo_inicio - self.tempo_chegada if self.tempo_inicio else 0
    
    def tempo_espera(self):
        return self.tempo_retorno() - self.duracao