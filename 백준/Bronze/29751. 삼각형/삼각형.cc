#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    double w, h;
    cin >> w >> h;
    double area = (w * h) / 2;

    cout << fixed;
    cout.precision(1);
    cout << area;

    return 0;
}