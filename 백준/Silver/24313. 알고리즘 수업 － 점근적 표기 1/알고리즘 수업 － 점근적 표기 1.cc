

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a_1, a_0, c, n_0;
    cin >> a_1 >> a_0;
    cin >> c;
    cin >> n_0;

    int f_result = (a_1 * n_0) + a_0;
    int g_result = c * n_0;

    if (f_result <= g_result && a_1 <= c) {
        cout << 1;
    }else {
        cout << 0;
    }

    return 0;
}
