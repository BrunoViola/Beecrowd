#include <stdio.h>
#include <string.h>

int main()
{
    char str[20], tam;
    scanf("%s", str);
    tam = strlen(str);
    
    if(tam>=10){
        printf("palavrao\n");
    } else{
        printf("palavrinha\n");
    }
    
    return 0;
}
