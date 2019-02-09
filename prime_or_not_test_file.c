#include<stdio.h>
int prime_or_not(int n);
int main()
{
    int primes[9] = {2,3,4,5,6,7,8,9,10},ans[9]={1,1,0,1,0,1,0,0,0};
    int i;
    for(i=0;i<9;i++){
        if(!(prime_or_not(primes[i])==ans[i])){
            printf("%d",primes[i]);
            return 0;
        }
    }
    printf("%d",-1);
}
