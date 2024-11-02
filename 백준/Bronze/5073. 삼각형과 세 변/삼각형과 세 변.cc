#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        int length[3] = {-1, -1, -1};
        for (int i = 0; i < 3; i++)
            cin >> length[i];

        if (
            length[0] == 0
            && length[1] == 0
            && length[2] == 0
            )
            break;

        if (
            length[0] == length[1]
            && length[1] == length[2]
            && length[2] == length[0]
            )
            cout << "Equilateral\n";
        else if (
            length[0] >= length[1] + length[2]
            || length[1] >= length[2] + length[0]
            || length[2] >= length[0] + length[1]
            )
            cout << "Invalid\n";
        else if (
            length[0] == length[1]
            || length[1] == length[2]
            || length[2] == length[0]
            )
            cout << "Isosceles\n";
        else if (
            length[0] != length[1]
            && length[1] != length[2]
            && length[2] != length[0]
            )
            cout << "Scalene\n";
    }

    return 0;
}