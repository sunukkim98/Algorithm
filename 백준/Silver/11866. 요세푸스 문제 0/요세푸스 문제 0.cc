
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

    int k, n;
    cin >> n >> k;

    queue<int> q, result;

    for (int i = 1; i <= n; i++) {
        q.push(i);
    }

    while (!q.empty()) {
        for (int i = 1; i <= k; i++) {
            if (i == k) {
                result.push(q.front());
                q.pop();
            } else {
                int front;
                front = q.front();
                q.pop();
                q.push(front);
            }
            // cout << "front" << i << ": " << q.front() << "\n";
            // cout << "queue size: " << q.size() << "\n";
        }
    }

    while (!result.empty()) {
        if (result.size() == 1 && n != 1) {
            cout << result.front() << ">";
        } else if (result.size() == n && n != 1) {
            cout << "<" << result.front() << ", ";
        } else if (n == 1) {
            cout << "<" << result.front() << ">";
        } else {
            cout << result.front() << ", ";
        }
        result.pop();
    }

    return 0;
}
