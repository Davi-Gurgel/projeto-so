# Sistemas Operacionais I - Projeto 01

## Descrição

Implementação de três algoritmos de escalonamento de CPU:

- **FCFS**: First-Come, First-Served (ordem de chegada)
- **SJF**: Shortest Job First (menor duração primeiro)
- **RR**: Round Robin (quantum = 2)

## Como Executar

```bash
python escalonador.py < entrada.txt
```

## Exemplo

**Entrada:**
```
0 10
4 4
8 6
21 8
```

**Saída:**
```
FCFS 10,0 3,0 3,0
SJF 10,0 3,0 3,0
RR 11,0 0,5 4,0
```

## Formato

- **Entrada**: `tempo_chegada duracao` (um processo por linha)
- **Saída**: `ALGORITMO tempo_retorno tempo_resposta tempo_espera`
