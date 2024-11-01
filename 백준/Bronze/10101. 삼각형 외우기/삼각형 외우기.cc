// 1 2 3
// 12 13
// 23

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int angle[3] = {0,};
    int sum = 0;
    for (int i = 0; i < 3; i++) {
        cin >> angle[i];
        sum += angle[i];
    }

    if (sum == 180) {
        int cnt = 0;
        for (int i = 2; i >= 0; i--) {
            for (int j = i-1; j >= 0; j--) {
                if (angle[i] == angle[j]) {
                    cnt++;
                }
            }
        }
        if (cnt == 0) {
            cout << "Scalene";
        }else if (cnt == 1 || cnt == 2) {
            cout << "Isosceles";
        }else if (cnt == 3) {
            cout << "Equilateral";
        }
    }else {
        cout << "Error";
    }

    return 0;
}