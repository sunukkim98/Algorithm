#include <iostream>

using namespace std;

string S;
string alphabet = "abcdefghijklmnopqrstuvwxyz";

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> S;
    int result[alphabet.length()];

    for (int i = 0; i < (int) alphabet.length(); i++) {
        result[i] = -1;
    }

    for (int i = 0; i < (int) S.length(); i++) {
        for (int j = 0; j < (int) alphabet.length(); j++) {
            if (result[j] < 0) {
                if (alphabet[j] == S[i]) {
                    result[j] = i;
                }
            }
        }
    }

    for (int i = 0; i < (int) alphabet.length(); i++) {
        cout << result[i] << " ";
    }

    return 0;
}

