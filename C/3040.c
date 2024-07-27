#include <stdio.h>

int main()
{
    int N, a, d, g;
    scanf("%d", &N);
    
    for(int i=0; i<N; i++){
        scanf("%d %d %d",&a,&d,&g);
        if(a>=200 && a<=300){
            if(d>=50){
                if(g>=150){
                    printf("Sim\n");
                }else{
                    printf("Nao\n");
                
                }
            }else{
                printf("Nao\n");
            }
        }else{
            printf("Nao\n");
        }
    }
    return 0;
}
