
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int A = 0, B = 0, C = 0;
    for (int i = 1; i <= N; i++) {
        A += i;
        C += i * i * i;
    }
    B = A * A;

    cout << A << "\n";
    cout << B << "\n";
    cout << C << "\n";


    return 0;
}

