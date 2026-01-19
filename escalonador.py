"""
Sistemas Operacionais I - Projeto 01
Algoritmos de Escalonamento de CPU: FCFS, SJF e Round Robin
"""

import sys
from collections import deque


class Processo:
    """Representa um processo no sistema."""
    
    def __init__(self, pid, tempo_chegada, duracao):
        self.pid = pid
        self.tempo_chegada = tempo_chegada
        self.duracao = duracao
        self.tempo_restante = duracao
        self.tempo_inicio = None
        self.tempo_fim = None
    
    @property
    def tempo_retorno(self):
        """Tempo total desde chegada até conclusão."""
        return self.tempo_fim - self.tempo_chegada if self.tempo_fim else 0
    
    @property
    def tempo_resposta(self):
        """Tempo desde chegada até primeira execução."""
        return self.tempo_inicio - self.tempo_chegada if self.tempo_inicio else 0
    
    @property
    def tempo_espera(self):
        """Tempo total aguardando na fila."""
        return self.tempo_retorno - self.duracao


def ler_entrada():
    """Lê processos da entrada padrão."""
    processos = []
    pid = 0
    for linha in sys.stdin:
        linha = linha.strip()
        if linha:
            partes = linha.split()
            if len(partes) >= 2:
                chegada = int(partes[0])
                duracao = int(partes[1])
                processos.append(Processo(pid, chegada, duracao))
                pid += 1
    return processos


def calcular_metricas(processos):
    """Calcula as métricas médias."""
    n = len(processos)
    if n == 0:
        return 0.0, 0.0, 0.0
    
    retorno = sum(p.tempo_retorno for p in processos) / n
    resposta = sum(p.tempo_resposta for p in processos) / n
    espera = sum(p.tempo_espera for p in processos) / n
    
    return retorno, resposta, espera


def fcfs(processos):
    """First-Come, First-Served - executa na ordem de chegada."""
    procs = [Processo(p.pid, p.tempo_chegada, p.duracao) for p in processos]
    procs.sort(key=lambda p: (p.tempo_chegada, p.pid))
    
    tempo = 0
    for p in procs:
        if tempo < p.tempo_chegada:
            tempo = p.tempo_chegada
        p.tempo_inicio = tempo
        tempo += p.duracao
        p.tempo_fim = tempo
    
    return calcular_metricas(procs)


def sjf(processos):
    """Shortest Job First - menor duração primeiro."""
    procs = [Processo(p.pid, p.tempo_chegada, p.duracao) for p in processos]
    completos = []
    tempo = 0
    
    while procs:
        disponiveis = [p for p in procs if p.tempo_chegada <= tempo]
        
        if not disponiveis:
            tempo = min(p.tempo_chegada for p in procs)
            continue
        
        escolhido = min(disponiveis, key=lambda p: (p.duracao, p.tempo_chegada, p.pid))
        procs.remove(escolhido)
        
        escolhido.tempo_inicio = tempo
        tempo += escolhido.duracao
        escolhido.tempo_fim = tempo
        completos.append(escolhido)
    
    return calcular_metricas(completos)


def round_robin(processos, quantum=2):
    """Round Robin - cada processo executa por um quantum de tempo."""
    procs = [Processo(p.pid, p.tempo_chegada, p.duracao) for p in processos]
    procs.sort(key=lambda p: (p.tempo_chegada, p.pid))
    
    fila = deque()
    nao_chegaram = list(procs)
    completos = []
    tempo = 0
    atual = None
    
    while nao_chegaram or fila or atual:
        # Adiciona processos que chegaram
        for p in list(nao_chegaram):
            if p.tempo_chegada <= tempo:
                nao_chegaram.remove(p)
                fila.append(p)
        
        # Pega próximo processo
        if atual is None:
            if fila:
                atual = fila.popleft()
            elif nao_chegaram:
                tempo = min(p.tempo_chegada for p in nao_chegaram)
                continue
            else:
                break
        
        # Marca início se primeira execução
        if atual.tempo_inicio is None:
            atual.tempo_inicio = tempo
        
        # Executa por quantum ou até terminar
        execucao = min(quantum, atual.tempo_restante)
        tempo += execucao
        atual.tempo_restante -= execucao
        
        # Adiciona processos que chegaram durante execução
        for p in list(nao_chegaram):
            if p.tempo_chegada <= tempo:
                nao_chegaram.remove(p)
                fila.append(p)
        
        # Verifica se terminou
        if atual.tempo_restante == 0:
            atual.tempo_fim = tempo
            completos.append(atual)
            atual = None
        else:
            fila.append(atual)
            atual = None
    
    return calcular_metricas(completos)


def formatar_saida(algoritmo, retorno, resposta, espera):
    """Formata a saída com vírgula como separador decimal."""
    return f"{algoritmo}: {retorno:.1f} {resposta:.1f} {espera:.1f}".replace('.', ',')


def main():
    processos = ler_entrada()
    
    if not processos:
        return
    
    # FCFS
    ret, resp, esp = fcfs(processos)
    print(formatar_saida("FCFS", ret, resp, esp))
    
    # SJF
    ret, resp, esp = sjf(processos)
    print(formatar_saida("SJF", ret, resp, esp))
    
    # Round Robin
    ret, resp, esp = round_robin(processos)
    print(formatar_saida("RR", ret, resp, esp))


if __name__ == "__main__":
    main()
