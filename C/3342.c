#include <stdio.h>

int main() {
    int tamanho, white, black;
    scanf ("%d", &tamanho);
    tamanho = tamanho * tamanho;
    if (tamanho%2==0){
        white = (tamanho)/2;
        printf ("%d casas brancas e %d casas pretas\n", white, white);

    } else {
        white = tamanho/2 +1;
        black = white - 1;
        printf ("%d casas brancas e %d casas pretas\n", white, black);
    }

    return 0;
}