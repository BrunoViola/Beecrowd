#include <stdio.h>

int main()
{
    int n, j, m, x, d;
    
    scanf("%d", &n);
    
    for(int i=0; i<n; i++){
        j=0; m=0;
        for(int l=0; l<3; l++){
            scanf("%d%d", &x, &d);
            j+=(x*d);
        }
        
        for(int k=0; k<3; k++){
            scanf("%d%d", &x, &d);
            m+=(x*d);
        }
        
        if(j>m){
            printf("JOAO\n");
        }else{
            printf("MARIA\n");
        }
    }
    return 0;
}
