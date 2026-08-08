#include <iostream>
#include <vector>
using namespace std;

double findMaxAverage(vector<int>& nums, int k) {
    int windowSum = 0;

    for(int i = 0; i<k; i++){
        windowSum += nums[i];
    }
    int maximum = windowSum;

    for(int i = k; i < nums.size(); i++) {
        windowSum -= nums[i - k];
        windowSum += nums[i];

        maximum = max(maximum, windowSum);
    }

    return (double)maximum / k;
}

int main(){
    vector<int> nums = {1,12,-5,-6,50,3};
    int k = 4;

    cout << findMaxAverage(nums, k);
    return 0;
}