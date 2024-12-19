#include<stack>
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    stack<int> s;

    for (int i = 0; i < n; i++) {
        string oper;
        cin >> oper;

        if (oper.compare("push") == 0) {
            int x;
            cin >> x;
            s.push(x);
        } else if (oper.compare("pop") == 0) {
            if (s.empty()) {
                cout << -1 << "\n";
            } else {
                cout << s.top() << "\n";
                s.pop();
            }
        } else if (oper.compare("size") == 0) {
            cout << s.size() << "\n";
        } else if (oper.compare("empty") == 0) {
            cout << s.empty() << "\n";
        } else if (oper.compare("top") == 0) {
            if (s.empty()) {
                cout << -1 << "\n";
            } else {
                cout << s.top() << "\n";
            }
        }
    }


    return 0;
}