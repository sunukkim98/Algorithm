
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string input;
    cin >> input;

    for (int i = 0; i <= input.length() / 2; i++) {
        if (input[i] != input[input.length() - i - 1]) {
            cout << 0;
            return 0;
        }
    }

    cout << 1;
    
    return 0;
}

