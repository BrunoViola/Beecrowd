#include <stdio.h>

int main()
{
    int qtd, resposta;
    scanf("%d", &qtd);
    for(int i=1; i<=qtd; i++){
        scanf("%d", &resposta);
        printf("resposta %d: %d\n", i, resposta);
    }
    
    return 0;
}
