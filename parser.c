#include <stdio.h>
#include <stdlib.h>

#include "parser.h"
#include "vetor.h"

int ordenar_por_chegada(const void* a, const void* b) {
	const Processo* p1 = (const Processo*)a;
	const Processo* p2 = (const Processo*)b;

	if (p1->t_chegada < p2->t_chegada) return -1;
    if (p1->t_chegada > p2->t_chegada) return 1;

    if (p1->id < p2->id) return -1;
    if (p1->id > p2->id) return 1;

	return 0;
}

int parse_arquivo(const char *nome_do_arquivo, VetorProcessos *processos) {
  	FILE *entrada = fopen(nome_do_arquivo, "r");

  	if (entrada == NULL) {
  		printf("\nFalha ao abrir arquivo: %s\n\n", nome_do_arquivo);
		return EXIT_FAILURE;
  	}

  	int chegada, pico;
  	int i = 0;
  	while (fscanf(entrada, "%d %d\n", &chegada, &pico) == 2) {
  	  	Processo temp = {
  	    	.id = i, 
		  	.t_chegada = chegada, 
		  	.t_pico = pico, 
		  	.t_restante = pico
	  	};
  	  	if (adicionar_processo(processos, temp) == EXIT_FAILURE) {
			fclose(entrada);
			return EXIT_FAILURE;
		} 
		
  	  	i++;
  	}
  	fclose(entrada);

	qsort(processos->dados, processos->tamanho, sizeof(Processo), ordenar_por_chegada);

  	return EXIT_SUCCESS;
}
