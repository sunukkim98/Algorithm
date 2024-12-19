#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    queue<int> q;

    for (int i = 0; i < n; i++) {
        string oper;
        cin >> oper;

        if (oper.compare("push") == 0) {
            int x;
            cin >> x;
            q.push(x);
        } else if (oper.compare("pop") == 0) {
            if (q.empty()) {
                cout << -1 << "\n";
            } else {
                cout << q.front() << "\n";
                q.pop();
            }
        } else if (oper.compare("size") == 0) {
            cout << q.size() << "\n";
        } else if (oper.compare("empty") == 0) {
            cout << q.empty() << "\n";
        } else if (oper.compare("front") == 0) {
            if (q.empty()) {
                cout << -1 << "\n";
            } else {
                cout << q.front() << "\n";
            }
        } else if (oper.compare("back") == 0) {
            if (q.empty()) {
                cout << -1 << "\n";
            } else {
                cout << q.back() << "\n";
            }
        }
    }


    return 0;
}