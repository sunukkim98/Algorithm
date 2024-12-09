
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

    int n, k;
    cin >> n >> k;

    int n_factorial = 1;
    for (int i = 1; i <= n; i++) {
        n_factorial *= i;
    }

    int k_factorial = 1;
    for (int i = 1; i <= k; i++) {
        k_factorial *= i;
    }

    int temp = n - k;
    int temp_factorial = 1;
    for (int i = 1; i <= temp; i++) {
        temp_factorial *= i;
    }

    int result = n_factorial / (k_factorial * temp_factorial);
    cout << result;

    return 0;
}
