#include <stdio.h>

int main() {
    int A, B, C, D, DIF;

    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &C);
    scanf("%d", &D);


    DIF = (A*B-C*D);

    printf("DIFERENCA = %d\n", DIF);

    return 0;
}