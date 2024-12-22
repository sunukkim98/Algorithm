#include <iostream>
#include <cmath>

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

    int length;
    cin >> length;

    int hash_val = 0;
    for (int i = 0; i < length; i++) {
        char alpahbet;
        cin >> alpahbet;
        int alphabet_to_int = int(alpahbet) - 96;
        // cout << alphabet_to_int;
        hash_val += alphabet_to_int * pow(31,i);
    }

    cout << hash_val;

    return 0;
}
