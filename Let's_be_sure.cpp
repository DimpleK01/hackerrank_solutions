#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int numberProblems(int sol[][3], int n){
    int sum,problems=0;
    for(int i=0; i<n; i++){
        sum=0;
        for(int j=0; j<3; j++){
            sum+=sol[i][j];
        }
        if(sum>=2){
           problems++; 
        }
    }
    return problems;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n;
    cin>>n;
    int sol[n][3];
    for(int i=0; i<n; i++){
        for(int j=0; j<3; j++){
            cin>>sol[i][j];
        }
    }
    cout<<numberProblems(sol, n);
    return 0;
}

