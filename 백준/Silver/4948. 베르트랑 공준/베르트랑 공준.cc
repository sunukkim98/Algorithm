
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

const int Max = 123456 * 2;

int main() {
    cout.tie(nullptr);
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    // false라면 소수
    bool arr[Max + 1] = {false};
    arr[1] = true;

    for (int i = 2; i * i <= Max; ++i) {
        //i의 배수 지우기
        if (!arr[i]) {
            for (int j = 2; i * j <= Max; ++j) {
                arr[i * j] = true;
            }
        }
    }

    int n;
    cin >> n;
    while (n) {
        int cnt = 0;
        for (int i = n + 1; i <= 2 * n; ++i) {
            //false의 개수 세기
            if (!arr[i]) ++cnt;
        }

        cout << cnt << '\n';
        cin >> n;
    }

    return 0;
}
