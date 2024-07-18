#include <stdio.h>

int main() {
    int horas, velmedia, dis;
    float qtdl;

    scanf("%d", &horas);
    scanf("%d", &velmedia);
    dis = horas*velmedia;
    qtdl = (float) dis/12;
    printf("%.3f\n", qtdl);

    return 0;
}