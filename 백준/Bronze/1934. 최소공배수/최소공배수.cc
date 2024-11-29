// 약수, 소수와 배수 2
// 1934번 최소공배수


#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <vector>
#include <set>

using namespace std;

int divide(int x, int y) {
    if (x % y == 0)
        return y;
    else
        return divide(y, x % y);
}
int main() {
    cout.tie(nullptr);
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    // int T; cin >> T;
    // int A, B;
    // int temp;
    // int j = 2;
    // set<int> divisors;
    // int least_common_multiple = 1;
    // for (int i = 0; i < T; i++) {
    //     cin >> A >> B;
    //     temp = A * B;
    //     while(temp != 1) {
    //         if (temp % j == 0) {
    //             divisors.insert(j);
    //             temp /= j;
    //             j = 2;
    //         }else {
    //             j++;
    //         }
    //     }
    //     for (set<int>::iterator iter = divisors.begin(); iter != divisors.end(); iter++) {
    //         least_common_multiple *= *iter;
    //     }
    //     cout << least_common_multiple << "\n";
    //     least_common_multiple = 1;
    // }

    int T;
    int A, B;
    cin >> T;

    for (int i = 0; i < T; i++) {
        cin >> A >> B;
        if (A >= B) {
            cout << A * B / divide(A, B) << "\n";
        } else {
            cout << A * B / divide(B, A) << "\n";
        }
    }

    return 0;
}
