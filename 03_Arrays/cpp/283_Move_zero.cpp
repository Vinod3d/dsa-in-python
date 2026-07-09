#include <iostream>
#include <vector>
using namespace std;

void moveZero(vector<int>& arr){
    int n = arr.size();
    int start = 0;

    for(int i = 0; i<n; i++){
        if(arr[i] != 0 ){
            swap(arr[i], arr[start]);
            start++;
        }
    }
    
    // Print the vector
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
}

int main(){
    vector<int> arr = {3, 0, 5, 0, 0, 6, 1, 0};

    moveZero(arr);
    return 0;
}