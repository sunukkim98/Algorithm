#include <iostream>
#include <deque>

using namespace std;

void print_deque(deque<int> dq, int n) {
    // print deque
    for (int i = 0; i < dq.size(); i++) {
        cout << dq[i] << " ";
    }
    cout << "\n";
    cout << "deque size: " << dq.size() << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    deque<pair<int, int>> dq;
    
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        dq.push_back(make_pair(num, i + 1));
    }

    while (!dq.empty()) {
        int idx = dq.front().first;
        cout << dq.front().second << " ";
        dq.pop_front();

        // deque이 비었다면 break
        if (dq.empty()) break;

        if (idx > 0) {
            for (int i = 0; i < idx - 1; i++) {
                dq.push_back(dq.front());
                dq.pop_front();
            }
        } else {
            for (int i = 0; i < -1 * idx; i++) {
                dq.push_front(dq.back());
                dq.pop_back();
            }
        }
    }

    return 0;
}