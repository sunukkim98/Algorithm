

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int x, y;
    int max_x = -10000, min_x = 10000;
    int max_y = -10000, min_y = 10000;

    for (int i = 0; i < N; i++) {
        cin >> x >> y;
        if (x >= max_x) max_x = x;
        if (x < min_x) min_x = x;
        if (y >= max_y) max_y = y;
        if (y < min_y) min_y = y;
    }

    cout << (max_x - min_x) * (max_y - min_y);

    return 0;
}