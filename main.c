#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <time.h>

long long contador=0;

void verificaAlgo(long long n) {
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
    printf("\nContador: %lld\n", contador);
}

void handler(int sinal) {
    printf("\nContador terminou em %lld\n", contador);
    exit(0);
}

int main() {
    signal(SIGINT, handler);
    clock_t inicio, fim;
    int quantidade;

    scanf("%d", &quantidade);

    inicio = clock();
    verificaAlgo(quantidade);
    fim = clock();

    double tempoExecucao = ((double) fim - inicio) / CLOCKS_PER_SEC;

    printf("\nTempo de execucao: %.3fs\n", tempoExecucao);
    return 0;
}