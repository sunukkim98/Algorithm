
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <vector>
#include <set>

using namespace std;

int GCD(int x, int y) {
    if (y == 0)
        return x;
    return GCD(y, x % y);
}

bool is_prime(long long n) {
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
    cout.tie(nullptr);
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    vector<int> arr, ascending, descending;
    int n;
    for (int i = 0; i < 8; i++) {
        cin >> n;
        arr.push_back(n);
        ascending.push_back(n);
        descending.push_back(n);
    }

    sort(ascending.begin(), ascending.end());
    sort(descending.begin(), descending.end(), compare);

    // for (int i = 0; i < 8; i++) {
    //     cout << descending[i] << " ";
    // }
    // cout << "\n";

    bool ascending_flag = true, descending_flag = true;
    for (int i = 0; i < 8; i++) {
        if (arr[i] != ascending[i]) {
            ascending_flag = false;
        }
        if (arr[i] != descending[i]) {
            descending_flag = false;
        }
    }

    // cout << "ascending: " << ascending_flag << "\tdescending: " << descending_flag << endl;

    if (ascending_flag) cout << "ascending";
    else if (descending_flag) cout << "descending";
    else cout << "mixed";

    return 0;
}
