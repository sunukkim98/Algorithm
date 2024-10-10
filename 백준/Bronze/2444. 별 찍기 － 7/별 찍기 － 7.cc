
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = N - i; j > 1; j--) {
            cout << " ";
        }
        for (int j = 1; j <= (2 * (i + 1)) - 1; j ++) {
            cout << "*";
        }
        cout << "\n";
    }
    for (int i = N - 1; i > 0; i--) {
        for (int j = 0; j < N - i; j++) {
            cout << " ";
        }
        for (int j = i + (i - 1); j > 0; j--) {
            cout << "*";
        }
        cout << "\n";
    }

    return 0;
}
