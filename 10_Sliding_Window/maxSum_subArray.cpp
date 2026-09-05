#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<int> nums = {1,2,3,4,5,6,7,8,9,10};
    int k = 3;

    int windowSum = 0;

    for(int i = 0; i < k; i++){
        windowSum += nums[i];
    }
    int maximum = windowSum;

    for(int i = k; i < nums.size(); i++){
        // windowSum -= nums[i - k];
        windowSum += nums[i] - nums[i - k];

        maximum = max(maximum, windowSum);
    }

    cout << maximum;
    return 0;
}