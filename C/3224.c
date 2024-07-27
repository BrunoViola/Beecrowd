#include <stdio.h>
#include <string.h>

int main()
{
    char str[1001];
    int pode, medico;
    scanf("%s", str);
    pode =strlen(str);
    scanf("%s", str);
    medico =strlen(str);
    
    if(medico>pode){
        printf("no\n");
    } else{
        printf("go\n");
    }
    
    
    return 0;
}
