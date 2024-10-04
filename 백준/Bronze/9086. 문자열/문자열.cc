#include <iostream>
#include <string>

using namespace std;

int T;

int main() {
    cin >> T;

    string word;
    for (int i = 0; i < T; i++) {
        cin >> word;
        cout << word[0] << word[(int) word.length() - 1] << "\n";
    }
    return 0;
}
