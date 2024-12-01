#include <iostream>
#include <map>
#include <vector>
#include <cctype>

using namespace std;

int GCD(int x, int y) {
    if (y == 0)
        return x;
    return GCD(y, x % y);
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int numerator_1, numerator_2, denominator_1, denominator_2;
    cin >> numerator_1 >> denominator_1;
    cin >> numerator_2 >> denominator_2;

    int result_numerator = numerator_1 * denominator_2 + numerator_2 * denominator_1;
    int result_denominator = denominator_1 * denominator_2;

    int gcd = GCD(result_numerator, result_denominator);
    cout << result_numerator / gcd << " " << result_denominator / gcd;
    return 0;
}
