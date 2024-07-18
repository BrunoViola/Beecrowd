#include <stdio.h>
#include <math.h>

int main() {
    double x1, y1, x2, y2,xmenosx, ymenosy, resultado, dentro;
    scanf ("%lf %lf", &x1, &y1);
    scanf ("%lf %lf", &x2, &y2);
    xmenosx = x2-x1;
    ymenosy = y2-y1;
    dentro = pow(xmenosx, 2) + pow(ymenosy, 2);
    resultado = pow(dentro,0.5);
    printf ("%.4lf\n", resultado);


    return 0;
}