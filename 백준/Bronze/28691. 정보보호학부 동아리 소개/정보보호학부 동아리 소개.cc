#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    char char_;
    cin >> char_;

    if (char_ == 'M')
        cout << "MatKor";
    if (char_ == 'W')
        cout << "WiCys";
    if (char_ == 'C')
        cout << "CyKor";
    if (char_ == 'A')
        cout << "AlKor";
    if (char_ == '$')
        cout << "$clear";

    return 0;
}