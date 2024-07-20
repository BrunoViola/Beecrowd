#include <stdio.h>

int main()
{
    int bPossui, galhos, qtd, faltam;
    scanf("%d", &bPossui);
    scanf("%d", &galhos);
    
    qtd = galhos/2;
    
    faltam = qtd-bPossui;
    
    if(faltam>0){
        printf("Faltam %d bolinha(s)\n", faltam);
    } else{
        printf("Amelia tem todas bolinhas!\n");
    }
    
    
    return 0;
}
