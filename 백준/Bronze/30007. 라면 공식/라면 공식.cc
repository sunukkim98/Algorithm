// 1 2 3
// 12 13
// 23

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        int A, B, X;
        cin >> A >> B >> X;
        cout << A*(X - 1) + B << "\n";
    }

    return 0;
}