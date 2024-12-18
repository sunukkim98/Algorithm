#include <deque>
#include <iostream>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    set<int> a;

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        a.insert(num);
    }

    int m;
    cin >> m;

    set<int>::iterator it;

    for (int i = 0; i < m; i++) {
        int key_num;
        cin >> key_num;
        it = a.find(key_num);
        if (it != a.end())
            cout << 1 << "\n";
        else {
            cout << 0 << "\n";
        }
    }

    return 0;
}