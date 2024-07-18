#include <stdio.h>

int main()
{
    int vetor[3], menor, posicao, maior, posMaior, medio;
    scanf("%d %d %d", &vetor[0], &vetor[1], &vetor[2]);
    menor=vetor[0];
    posicao=0;
    maior=vetor[0];
    posMaior=0;
    for(int i = 0; i<3; i++){
        if(vetor[i]<menor){
            menor = vetor[i];
            posicao = i;
        }
        if(vetor[i]>maior){
            maior=vetor[i];
            posMaior = i;
        } 
    }
    
    medio = posicao+posMaior;
    switch(medio){
        case 3:
            printf("huguinho\n");
        break;
        case 2:
            printf("zezinho\n");
        break;
        case 1:
            printf("luisinho\n");
        break;
    }
    return 0;
}
