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

    int a, b, c;
    cin >> a >> b >> c;
    int multiply = a * b * c;
    string str = to_string(multiply);
    int cnt[11] = {0,};
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == '0') {
            cnt[0]++;
        } else if (str[i] == '1') {
            cnt[1]++;
        } else if (str[i] == '2') {
            cnt[2]++;
        } else if (str[i] == '3') {
            cnt[3]++;
        } else if (str[i] == '4') {
            cnt[4]++;
        } else if (str[i] == '5') {
            cnt[5]++;
        } else if (str[i] == '6') {
            cnt[6]++;
        } else if (str[i] == '7') {
            cnt[7]++;
        } else if (str[i] == '8') {
            cnt[8]++;
        } else if (str[i] == '9') {
            cnt[9]++;
        }
    }

    for (int i = 0; i < 10; i++) {
        cout << cnt[i] << "\n";
    }
    return 0;
}
