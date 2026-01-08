#ifndef VETOR_H
#define VETOR_H

#include <stdlib.h>

typedef struct {
	int id;
	int t_chegada;
	int t_pico;
	int t_restante;
} Processo;

typedef struct {
	Processo* dados;
	size_t tamanho;
	size_t capacidade;
} VetorProcessos;

VetorProcessos* criar_vetor(size_t capacidade_inicial);
int adicionar_processo(VetorProcessos* vetor, Processo p);
void free_vetor(VetorProcessos* vetor);

#endif // !VETOR_H
