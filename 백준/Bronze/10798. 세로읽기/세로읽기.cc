// 00 01 02 03 04
// 10 11 12 13 14
// 20 21 22 23 24
// 30 31 32 33 34
// 40 41 42 43 44


#include <iostream>
#include <string>

using namespace std;

char matrix[5][15];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int i = 0; i < 5; i++) {
        cin >> matrix[i];
    }

    for (int i = 0; i < 15; i++) {
        for (int j = 0; j < 5; j++) {
            if (matrix[j][i] != NULL) {
                cout << matrix[j][i];
            }
        }
    }

    return 0;
}

