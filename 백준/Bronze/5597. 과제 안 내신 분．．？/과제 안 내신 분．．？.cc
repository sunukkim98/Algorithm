#include <iostream>
#include <string>

using namespace std;

int main() {
    bool student[30];
    int register_idx;

    for (int i = 0; i < 30; i++) {
        student[i] = false;
    }

    for (int i = 0; i < 28; i++) {
        cin >> register_idx;
        student[register_idx - 1] = true;
    }

    for (int i = 0; i < 30; i++) {
        if (student[i] == false) {
            cout << i + 1 << "\n";
        }
    }

    return 0;
}
