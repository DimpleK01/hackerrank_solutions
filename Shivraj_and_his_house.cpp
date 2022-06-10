#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int minDoors(int arr[], int n){
    int left,right,lcheck,rcheck,ans;
    left=right=lcheck=rcheck=ans=0;
    
    for(int i=0; i<n; i++){
        if(arr[i]==0){
            left++;
        }
        else right++;
    }
    for(int i=0; i<n; i++){
        ans++;
        if(arr[i]==0){
            lcheck++;
            if(lcheck==left){
                 break;
             }
        }
        else {
            rcheck++;
            if(rcheck==right){
                 break;
             }
        }
    }
    return ans;
    
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n;
    cin>>n;
    int arr[n];
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
    cout<<minDoors(arr, n);
    return 0;
}

