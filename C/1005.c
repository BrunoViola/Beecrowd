#include <stdio.h>

int main() {
    double A, B, media;

    scanf("%lf", &A);
    scanf("%lf", &B);

    media = (3.5*A + B*7.5)/11;

    printf("MEDIA = %.5lf\n", media);

    return 0;
}
