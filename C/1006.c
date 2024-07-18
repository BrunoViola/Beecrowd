#include <stdio.h>

int main() {
    double A, B, C, media;

    scanf("%lf", &A);
    scanf("%lf", &B);
    scanf("%lf", &C);


    media = (2*A + B*3 + C*5)/10;

    printf("MEDIA = %.1lf\n", media);

    return 0;
}
