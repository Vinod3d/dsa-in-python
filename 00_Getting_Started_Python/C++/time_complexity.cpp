#include <iostream>
using namespace std;

int main() {
    int n;
    int m = 5;

    for(int i = 0; i<m; i++){ // O(1) constant time complexity
        cout << i << " ";
    }
    cout << endl;


    for(int i = 0; i<n; i++){ // O(n) time complexity
        cout << i << " ";
    }
    cout << endl;

    for(int i = 0; i<n; i*2){ // O(log n) time complexity
        cout << i << " ";
    }
    cout << endl;

    for(int i = 0; i<n; i++){
        for(int j = 0; j<n; j*2){ // O(n log n) time complexity
            cout << i << " " << j << " ";
        }
        cout << endl;
    }

    for(int i = 0; i<n; i++){
        for(int j = 0; j<i; j++){ // O(n^2) time complexity
            cout << i << " " << j << " ";
        }
        cout << endl;
    }


    return 0;
}