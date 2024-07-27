#include <stdio.h>

int main()
{
    int N, a, d, g;
    
    scanf("%d %d %d",&a,&d,&g);
    N = a-d-g;
    
    if(N>d && N>g){
    printf("%d\n", N);
    }else if(d>N && d>g){
    printf("%d\n", d);
    }else if(g>d && g>N){
    printf("%d\n", g);
    }
    return 0;
}
