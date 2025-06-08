#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <time.h>

long long contador=0;

void verificaAlgo(int n) {
    // reset do contador
    contador = 0;

    int i, j, k, l;
    for (l = 1; l <= 10000; l++) {
        for (i=1; i <= n -5; i++) {
            for (j = i+2; j <= n/2; j++) {
                for (k = 1; k <= n; k++) {
                    contador++;
                }
            }
        }
    }
    printf("\nPara N = %d, Contador: %lld\n", n, contador);
}

void handler(int sinal) {
    printf("\nContador terminou em %lld\n", contador);
    exit(0);
}

int main() {
    signal(SIGINT, handler);
    clock_t inicio, fim;
    int quantidade;

    // quantos testes vamos realizar
    int quantidade_testes[] = {10, 25, 30, 50, 100, 200};
    int tamanho = sizeof(quantidade_testes) / sizeof(quantidade_testes[0]);


    // execucao da funcao em si
    inicio = clock();
    for (int i=0; i < tamanho; i++) {
        verificaAlgo(quantidade_testes[i]);
    }
    fim = clock();

    double tempoExecucao = ((double) fim - inicio) / CLOCKS_PER_SEC;

    printf("\nTempo de execucao: %.3fs\n", tempoExecucao);
    return 0;
}
