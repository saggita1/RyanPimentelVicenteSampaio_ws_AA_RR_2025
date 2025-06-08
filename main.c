#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <time.h>

long long contador=0;

void verificaAlgo(int n, FILE *arquivo) {
    clock_t inicio, fim;

    // reset do contador
    contador = 0;

    int i, j, k, l;

    inicio = clock();
    for (l = 1; l <= 10000; l++) {
        for (i=1; i <= n -5; i++) {
            for (j = i+2; j <= n/2; j++) {
                for (k = 1; k <= n; k++) {
                    contador++;
                }
            }
        }
    }
    fim = clock();
    double tempoExecucao = ((double) fim - inicio) / CLOCKS_PER_SEC;

    printf("\nPara N = %d, Contador: %lld", n, contador);
    printf("\nTempo de execucao para N=%d: %.3fs\n", n, tempoExecucao);

    // escrevendo no csv
    fprintf(arquivo, "%d, %lld, %.3f\n", n, contador, tempoExecucao);
}

void handler(int sinal) {
    printf("\nContador terminou em %lld\n", contador);
    exit(0);
}

int main() {
    signal(SIGINT, handler);
    int quantidade;
    FILE *arquivo; // ponteiro pro arquivo csv

    // abrindo e escrevendo cabeçalho
    arquivo = fopen("resultados.csv", "w");
    fprintf(arquivo, "N, Contador, Tempo de execução\n");


    // quantos testes vamos realizar
    int quantidade_testes[] = {1000, 10000, 100000, 1000000};
    int tamanho = sizeof(quantidade_testes) / sizeof(quantidade_testes[0]);


    // execucao da funcao em si
    for (int i=0; i < tamanho; i++) {
        verificaAlgo(quantidade_testes[i], arquivo);
    }
    
    // fechando arquivo
    fclose(arquivo);
    printf("\nResultados salvos em resultados.csv\n");
    return 0;
}
