#include <stdio.h>
 
#include <stdio.h>

int main() {
    double raio, area, pi;

    scanf("%lf", &raio);
    pi=3.14159;
    area = pi*raio*raio;
    printf("A=%.4f\n", area);

    return 0;
}