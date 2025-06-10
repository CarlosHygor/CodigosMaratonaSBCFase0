#include <stdio.h>

int main()
{

    long long int x, y, k, div, i, j, resumo;
    x = 1;
    scanf("%lli %lli", &y, &k);
    div = 1;
    resumo = y+1 / 2;
    for(i=1;i<=k;i++){
        if (x % y == 0){
            div = y;
        }
        else {
            if(y%2 != 0 || x%2 != 0){
                for(j=resumo;j>=1;j=j-2){
                    if((x%j==0) && (y%j==0)){
                        div = j;
                        break;
                    }
                }
            }

            else{
                for(j=resumo;j>=1;j=j-1){
                    if((x%j==0) && (y%j==0)){
                        div = j;
                        break;
                    }
                }
            }

        }
        x += div;
    }
    printf("%lli", x);
}
