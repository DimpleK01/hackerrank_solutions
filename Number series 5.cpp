
#include "bits/stdc++.h"
using namespace std;

void printSeries(int n, int a,int b, int c){

    int d;

    if (n == 1) {
        cout << a << " ";
        return;
    }
    if (n == 2) {
        cout << a << " " << b << " ";
        return;
    }

    cout << a << " " << b
        << " " << c << " ";

    for (int i = 4; i <= n; i++) {
        d = a + b + c;
        a = b;
        b = c;
        c = d;
        cout << d << " ";
    }
}

// Driver Code
int main()
{
    int p,L, a = 1, b = 2, c = 5;
    cin>>p;
    for(int i=0;i<p;i++){
        cin>>L;
        printSeries(L, a, b, c);
        cout<<"\n";
    }
    return 0;
}
