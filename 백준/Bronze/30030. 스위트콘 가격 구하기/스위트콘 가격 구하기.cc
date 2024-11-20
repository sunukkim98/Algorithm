#include <iostream>
#include <string>
#include <algorithm>
#include <utility>
// 100 + 1000 = 1100
// 101 + 1010 =  1111
// 102 + 1020 = 1122
// 103 + 1030 = 1133
// 9000 + 900 = 9900
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int B;
    cin >> B;

    int ans = 0;

    for (int i = 100; i < 901; i++) {
        if (B == (i) + (i * 10))
            ans = (i * 10);
    }

    cout << ans;

    return 0;
}
