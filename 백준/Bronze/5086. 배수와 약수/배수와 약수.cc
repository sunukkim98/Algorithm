

#include <iostream>

using namespace std;

int a, b;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (1) {
        cin >> a >> b;
        if (a == 0 && b == 0) break;
        if (a % b == 0) {
            cout << "multiple\n";
        }else if (b % a == 0) {
            cout << "factor\n";
        }else {
            cout << "neither\n";
        }
    }

    return 0;
}