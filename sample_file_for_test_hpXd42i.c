#include<stdio.h>
int even_or_odd(int n);
int main(){

    int array[10] = {2,3,4,5,6,7,8,9,10,11},result[10]={1,0,1,0,1,0,1,0,1,0},iter;
    for(iter=0;iter<10;iter++){
        if(even_or_odd(array[iter])!=result[iter]){
            printf("%d",array[iter]);
            return 0;
        }
    }
    printf("%d",-1);
    return 0;
}
