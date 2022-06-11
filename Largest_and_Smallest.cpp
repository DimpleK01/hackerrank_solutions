#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int maxminDiff(int arr[], int n){
    int max,min;
    max=min=arr[0];
    int max_i,min_i;
    max_i=min_i=0;
    
    for(int i=0; i<n; i++){
        if(arr[i]>=max){
            max=arr[i];
            max_i=i;
        }
        else if (arr[i]<=min){
            min = arr[i];
            min_i=i;
        }
    }
    return max_i-min_i;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin>>n;
    int arr[n];
    for(int i=0; i<n;i++){
        cin>>arr[i];
    }
    cout<<maxminDiff(arr, n);
    return 0;
}
