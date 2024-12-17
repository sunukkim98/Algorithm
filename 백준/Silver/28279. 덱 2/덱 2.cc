#include <deque>
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    deque<int> dq;

    for (int i = 0; i < n; i++) {
        int order;
        cin >> order;

        if (order == 1) {
            int num;
            cin >> num;
            dq.push_front(num);
        } else if (order == 2) {
            int num;
            cin >> num;
            dq.push_back(num);
        } else if (order == 3) {
            if (dq.empty()) {
                cout << -1 << "\n";
            } else {
                cout << dq.front() << "\n";
                dq.pop_front();
            }
        } else if (order == 4) {
            if (dq.empty()) {
                cout << -1 << "\n";
            } else {
                cout << dq.back() << "\n";
                dq.pop_back();
            }
        } else if (order == 5) {
            cout << dq.size() << "\n";
        } else if (order == 6) {
            cout << dq.empty() << "\n";
        } else if (order == 7) {
            if (dq.empty()) {
                cout << -1 << "\n";
            } else {
                cout << dq.front() << "\n";
            }
        } else if (order == 8) {
            if (dq.empty()) {
                cout << -1 << "\n";
            } else {
                cout << dq.back() << "\n";
            }
        }
    }
    return 0;
}