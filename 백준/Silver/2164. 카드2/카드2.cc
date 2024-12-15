
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

    for (int i = 1; i <= n; i++) {
        q.push(i);
    }

    int result = -1;
    while (1) {
        if (q.size() == 1) break;
        int front = q.front();
        // cout << "front1: " << front << "\n";
        q.pop();
        front = q.front();
        // cout << "front2: " << front << "\n";
        q.pop();
        q.push(front);
    }

    // cout << q.size();
    if (q.size() == 1) {
        cout << q.front();
    }

    return 0;
}
