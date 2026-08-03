#include <iostream>
#include <set>
using namespace std;

int main() {
    
    set<int> s;
    s.insert(1);
    s.insert(2);
    s.insert(3);
    s.insert(1);
    s.erase(2);
    s.erase(s.begin());

    cout << s.size() << endl;
    cout << s.count(2) << endl;
    
    for(int x: s) {
        cout << x << " ";
    }
    
    return 0;
}
