#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    int arr[] = {2,7,11,15};
    int n = 4;
    int target = 9;
    
    unordered_map<int,int> seen; 
    for(int i = 0; i < n ; ++i){
        int complement = target - arr[i];
        if(seen.find(complement) != seen.end()){
            cout << seen[complement] << " " << i << endl;
        }
        seen[arr[i]] = i;
    }
    return 0;
}