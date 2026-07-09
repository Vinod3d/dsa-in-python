#include <iostream>
#include <vector>
using namespace std

bestTime(vector<in>& stocks){
    int n = stocks.size();
    int profit = 0;
    int minStock = stocks[0];

    for(int i = 1; i<n; i++){
        int currentProfit = stocks[i] - minStock;
        if(currentProfit > profit) profit = currentProfit;
        minStock = min(minStock, stocks[i]);
    }
    cout << profit;
}

int main(){
    vector<int> stocks = {7, 1, 5, 3, 6, 4};
    bestTime(stocks);
    return 0;
}