// #include <iostream>
// #include <vector>
// using namespace std;

// int main() {
//     vector<int> arr = {1,1,2,2,3,3};

//     int k = 1;

//     for(int i = 1; i < arr.size(); i++) {
//         if(arr[i] != arr[i-1]) {
//             arr[k] = arr[i];
//             k++;
//         }
//     }

//     cout << "Unique count: " << k << endl;

//     for(int i = 0; i < k; i++) {
//         cout << arr[i] << " ";
//     }

//     cout << endl;

//     return 0;
// }



#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> arr = {1,1,2,2,3,3};

    int k = 1;

    for(int i = 1; i < arr.size(); i++) {
        if(arr[i] != arr[i-1]) {
            arr[k] = arr[i];
            k++;
        }
    }

    cout << "Unique count: " << k << endl;

    for(int i = 0; i < k; i++) {
        cout << arr[i] << " ";
    }

    cout << endl;

    return 0;
}