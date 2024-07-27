#include <stdio.h>

int main()
{
    char str[10], gen;
    int qtd, carrinhos=0, bonecas=0;
    scanf("%d", &qtd);
    for(int i=1; i<=qtd; i++){
        scanf("%s %c", str, &gen);
     
        if(gen == 'M'){
            carrinhos++;
        } else{
            bonecas++;
        }
    }
    
    printf("%d carrinhos\n%d bonecas\n", carrinhos, bonecas);
    return 0;
}
