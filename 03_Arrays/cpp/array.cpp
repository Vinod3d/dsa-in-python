#include <iostream>
#include <vector> // array 
#include <algorithm> // 

using namespace std;

void printArray(const vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    printArray(arr);
    return 0;
}