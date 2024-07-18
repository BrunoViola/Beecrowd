#include <stdio.h>
int main() {
    int cod1, cod2, num1, num2;
    float valor1, valor2, soma;

    scanf ("%d",&cod1);
    scanf ("%d",&num1);
    scanf ("%f",&valor1);
    scanf ("%d",&cod2);
    scanf ("%d",&num2);
    scanf ("%f",&valor2);
    soma = num1*valor1+num2*valor2;
    printf("VALOR A PAGAR: R$ %.2f\n", soma);

    return 0;
}