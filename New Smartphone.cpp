#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
int bestDealer(int n, long a[]){
    int min=a[0], index=0;
    for(int i=0; i<n; i++){
        if (a[i]<min){
            min=a[i];
            index=i;
        }
    }
    return index;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    scanf("%d",&n);
    long a[n];
    for(int i=0; i<n; i++){
        scanf("%ld",&a[i]);  
    }
    printf("dealer%d",bestDealer(n, a));
    return 0;
}
