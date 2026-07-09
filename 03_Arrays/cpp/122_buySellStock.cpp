#include <iostream>
#include <vector>
using namespace std

bestTime(vector<in>& stocks){
    int n = stocks.size();
    int ans = 0;

    for(int i = 0; i<n; i++){
        if(stocks[i] < stocks[i + 1]){
            ans += stocks[i +1] - stocks[i];
        }
    }

    cout << ans;
}

int main(){
    vector<int> stocks = {7, 1, 5, 3, 6, 4};
    bestTime(stocks);
    return 0;
}