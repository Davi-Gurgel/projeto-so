#include <stdio.h>
#include <stdlib.h>

#include "vetor.h"

VetorProcessos* criar_vetor(size_t capacidade_inicial) 
{
	// size_t e unsigned (nunca e negativo)
	if (capacidade_inicial == 0) return NULL;

	VetorProcessos* vetor = (VetorProcessos*)malloc(sizeof(VetorProcessos));
	if (!vetor) return NULL;
	
	vetor->capacidade = capacidade_inicial;
	vetor->tamanho = 0;
	vetor->dados = (Processo*)malloc(sizeof(Processo) * vetor->capacidade);
	if (!vetor->dados) { 
		free(vetor);
		return NULL;
	}

	return vetor;
}

int adicionar_processo(VetorProcessos *vetor, Processo p)
{
	if (vetor->capacidade == vetor->tamanho) {
		size_t nova_capacidade = vetor->capacidade * 2;

		Processo* aux = (Processo*)realloc(vetor->dados,sizeof(Processo) * nova_capacidade);
		if (!aux) return EXIT_FAILURE;

		vetor->dados = aux;
		vetor->capacidade = nova_capacidade;
	}
	
	vetor->dados[vetor->tamanho] = p;
	vetor->tamanho++;

	return EXIT_SUCCESS;
}

void free_vetor(VetorProcessos *vetor) 
{
	if (vetor == NULL) return;
	free(vetor->dados);
	free(vetor);
}
