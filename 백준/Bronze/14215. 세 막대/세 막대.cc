

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int length[3] = {0,};
    for (int i = 0; i < 3; i ++) {
        cin >> length[i];
    }

    sort(length, length+3);

    if (length[0] + length[1] <= length[2])
        length[2] = length[0] + length[1] - 1;

    cout << length[0] + length[1] + length[2];

    return 0;
}
