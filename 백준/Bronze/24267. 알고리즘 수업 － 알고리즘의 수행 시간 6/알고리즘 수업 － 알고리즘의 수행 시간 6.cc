

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    cin >> n;
    cout << ((n - 2) * (n - 1) * n) / 6 << "\n" << 3;

    return 0;
}
