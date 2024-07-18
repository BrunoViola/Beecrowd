#include <stdio.h>
int main() {
    int numf, numht;
    float valor, sal;

    scanf ("%d",&numf);
    scanf ("%d",&numht);
    scanf ("%f",&valor);

    sal = numht*valor;
    printf("NUMBER = %d\nSALARY = U$ %.2f\n", numf, sal);

    return 0;
}