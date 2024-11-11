

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, c, d, e, f;
    int x, y;

    cin >> a >> b >> c >> d >> e >> f;

    x = ((c*e) - (b*f)) / ((e*a) - (b*d));
    y = ((c*d) - (a*f)) / ((b*d) - (a*e));

    cout << x << " " << y;

    return 0;
}
