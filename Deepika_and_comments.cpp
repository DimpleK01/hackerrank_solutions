#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void getResult(int votes[3]){
    if(votes[0]==votes[1] && votes[2]==0)
        cout<<"0";
    else if (votes[0]>(votes[1]+votes[2]))
        cout<<"+";
    else if (votes[1]>(votes[0]+votes[2]))
        cout<<"-";
    else
        cout<<"?";
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int votes[3];
    for(int i=0; i<3; i++)
        cin>>votes[i];
    getResult(votes);
    return 0;
}

