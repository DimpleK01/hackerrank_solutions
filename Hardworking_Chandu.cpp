#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void serverStatus(int commands[][3], int n){
    int serverA, serverB, success_A, success_B;
    serverA=serverB=success_A=success_B=0;
    for(int i=0; i<n; i++){
        if(commands[i][0]==1){
            serverA++;
            success_A+=commands[i][1];
        }
        else{
            serverB++;
            success_B+=commands[i][1];
        }      
    }
    
    if(success_A>=(serverA*10)/2)
        cout<<"LIVE\n";
    else cout<<"DEAD\n";
    
    if(success_B>=(serverB*10)/2)
        cout<<"LIVE";
    else cout<<"DEAD";
        
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n;
    cin>>n;
    int commands[n][3];
    for(int i=0; i<n; i++){
        for(int j=0; j<3; j++){
            cin>>commands[i][j];
        }
    }
    serverStatus(commands, n);
    return 0;
}

