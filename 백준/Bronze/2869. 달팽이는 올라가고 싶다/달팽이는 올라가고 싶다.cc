// 1
// 2 - 1 = 1
// 2
// 1 + 2 - 1 = 2
// 3
// 2 + 2 - 1 = 3
// 4

#include <iostream>

using namespace std;

int A, B, V;
int days = 1;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> A >> B >> V;

    days += (V - A) / (A - B);
    if ((V - A) % (A - B) != 0) days++;
    if (A >= V) cout << '1';
    else cout << days;

    return 0;
}