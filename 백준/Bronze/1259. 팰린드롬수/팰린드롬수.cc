
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

    int num;
    string str_num;
    bool flag = true;
    while(1) {
        cin >> num;
        if (num == 0) break;
        str_num = to_string(num);
        for (int i = 0; i <= str_num.size() / 2; i++) {
            if (str_num[i] != str_num[str_num.size() - i - 1]) {
                flag = false;
                break;
            }
        }
        if (flag) {
            cout << "yes\n";
        }else {
            cout << "no\n";
        }
        flag = true;
    }

    return 0;
}
