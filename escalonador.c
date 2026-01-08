#include <stdio.h>
#include <stdlib.h> 

#include "parser.h"
#include "vetor.h"

#define EXPECTED_ARGS 2

int main(int argc, char *argv[])
{
    if (argc != EXPECTED_ARGS) {
        printf("\nUso correto: %s <arquivo>\n\n", argv[0]);
        return EXIT_FAILURE;
    }
    
    VetorProcessos* processos = criar_vetor(64);
    if (!processos) return EXIT_FAILURE;

    if (parse_arquivo(argv[1], processos) == EXIT_FAILURE) {
        free_vetor(processos); 
        return EXIT_FAILURE;
    }


    free_vetor(processos);
    return EXIT_SUCCESS;
}
