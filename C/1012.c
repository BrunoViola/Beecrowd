#include <stdio.h>

int main() {
    double a, b, c, trian, circ, trap, quad, retan, pi;
    pi = 3.14159;
    scanf("%lf %lf %lf",&a, &b, &c);

    trian = (a*c)/2;
    circ = pi * c *c;
    trap = ((a+b)*c)/2;
    quad = b*b;
    retan = a*b;

    printf("TRIANGULO: %.3lf\nCIRCULO: %.3lf\nTRAPEZIO: %.3lf\nQUADRADO: %.3lf\nRETANGULO: %.3lf\n", trian, circ, trap, quad, retan);

    return 0;
}