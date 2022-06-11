#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

string removeDuplicates(string digits){
    bool flag=true;
    int duplicates;
    for(int i=0; i<int(digits.length()-1); i++){
        duplicates=1;
        flag=true;
        for(int j=i+1; j<int(digits.length()); j++){
            if(digits[i]==digits[j]){
                duplicates++;
                flag=false;
            }
            else{
                break;
            }
               }
        if(flag==false){
            digits.erase(i,duplicates);
            break;
        }
    }
               
    
    if(digits==""){
        return "-1";
    }
    else if (flag==true){
        return digits;
    }
    else{
        return removeDuplicates(digits); 
    }
    
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    string digits;
    cin>>digits;
    cout<<removeDuplicates(digits);
    return 0;
    
}
