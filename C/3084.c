#include <stdio.h>

int main()
{
    int x, d, hora, minuto;

    while(scanf("%d%d", &x, &d)!=EOF){
        hora=x/30;
        minuto=d/6;
        
        if(hora<10){
            if(minuto<10){
                printf("0%d:0%d\n", hora, minuto);
            }else{
                printf("0%d:%d\n", hora, minuto);
            }
        }else{
            if(minuto<10){
                printf("%d:0%d\n", hora, minuto);
            }else{
                printf("%d:%d\n", hora, minuto);
            }
        }
    }
    return 0;
}
