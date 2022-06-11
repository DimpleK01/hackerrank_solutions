#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int diagonalProduct(int n, int matrix[][n]) {
    int l_sum=0,r_sum=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(i==j){
                l_sum+=matrix[i][j];
            }
            if(i+j==n-1){
                r_sum+=matrix[i][j];
            }
        }
    }
    return l_sum*r_sum;  
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    scanf("%d",&n);

    
    
    int matrix[n][n];
    
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&matrix[i][j]);
        }
    }
    printf("%d", diagonalProduct(n,matrix));
    
    
    return 0;
}
