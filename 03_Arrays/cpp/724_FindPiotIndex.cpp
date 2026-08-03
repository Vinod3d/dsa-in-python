#include <iostream>
#include <vector>
using namespace std;

int findPiotIndex(vector<int>& arr){
    int n = arr.size();
    int leftSum = 0;
    int rightSum = 0;

    // Calculate the right sum
    for(int i = 0; i<n; i++){
        rightSum += arr[i];
    }

    for(int i = 0; i<n; i++){
        rightSum -= arr[i];
        if(leftSum == rightSum){
            return i;
        }
        leftSum += arr[i];
    }
    
    return -1;
}

int main(){
    vector<int> arr = {1, 7, 3, 6, 5, 6};

    cout << findPiotIndex(arr) << endl;
    return 0;
}
