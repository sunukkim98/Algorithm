
#include <iostream>
#include <string>
#include <queue>

using namespace std;

int GCD(int x, int y) {
    if (y == 0)
        return x;
    return GCD(y, x % y);
}

bool check_prime(long long n) {
    if (n <= 1) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i++) {
        if (n % i == 0 || n % (i + 2) == 0){
            return false;
        }
    }
    return true;
}

bool compare(int x, int y) {
    return y < x;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;

    queue<int> q;
    int num;

    string operation;
    for (int i = 0; i < n; i++) {
        cin >> operation;
        if (operation.compare("push") == 0) {
            cin >> num;
            q.push(num);
        } else if (operation.compare("pop") == 0) {
            if (q.empty()) {
                cout << -1 << "\n";
            }else {
                cout << q.front() << "\n";
                q.pop();
            }
        } else if (operation.compare("size") == 0) {
            cout << q.size() << "\n";
        } else if (operation.compare("empty") == 0) {
            cout << q.empty() << "\n";
        } else if (operation.compare("front") == 0) {
            if (q.empty()) {
                cout << -1 << "\n";
            }else {
                cout << q.front() << "\n";
            }
        } else if (operation.compare("back") == 0) {
            if (q.empty()) {
                cout << -1 << "\n";
            }else {
                cout << q.back() << "\n";
            }
        }
    }

    return 0;
}
