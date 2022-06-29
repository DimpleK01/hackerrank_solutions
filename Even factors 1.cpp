#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;
void evenFactors(int n){
    bool flag =false;
    for(int i=2; i<=n; i++){
        if((n%i==0) && (i%2==0)){
            flag=true;
            cout<<i<<" ";
        }
        else{
            continue;
        } 
    }
    if(flag==false){
        cout<<"-1";
    }
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin>>n;
    evenFactors(n);
    return 0;
}
