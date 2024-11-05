#include <iostream>
#include <cmath>

using namespace std;

int main() {
    long long N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        double d, f, p;
        cin >> d >> f >> p;

        cout << fixed;
        cout.precision(2);
        cout << "$" << f * d * p << "\n";
    }

    return 0;
}
