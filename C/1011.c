#include <stdio.h>

int main() {
    double raio, vol, pi;

    scanf("%lf", &raio);

    pi = 3.14159;
    vol = (4/3.0)*pi*raio*raio*raio;

    printf("VOLUME = %.3lf\n", vol);

    return 0;
}