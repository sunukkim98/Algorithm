
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <vector>
#include <set>
#include<stack>

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

    int k;
    cin >> k;
    int num;
    stack<int> stk;

    for (int i = 0; i < k; i++) {
        cin >> num;
        if (num == 0) {
            stk.pop();
        }else {
            stk.push(num);
        }
    }

    int sum = 0;
    while (!stk.empty()) {
        sum += stk.top();
        stk.pop();
    }

    cout << sum;

    return 0;
}
