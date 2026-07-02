#include <iostream>
#include <vector>
using namespace std;

void printSubsets(vector<int> arr, int index, vector<int> current){
    if(index == arr.size()){
        cout << "[";
        for (int num : current) {
            cout << num << " ";
        }
        cout << "]\n";
        return;
    }

    // Include the element at the current index
    current.push_back(arr[index]);
    printSubsets(arr, index + 1, current);

    // Exclude the element at the current index
    current.pop_back();
    printSubsets(arr, index + 1, current);
    
}

int main(){
    vector<int> arr = {1, 2, 3};
    vector<int> current;
    printSubsets(arr, 0, current);

    return 0;
}