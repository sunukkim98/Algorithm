

#include <iostream>
#include <algorithm>


using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int num[5];
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        cin >> num[i];
        sum += num[i];
    }
    sort(num, num+5);

    cout << sum / 5 << "\n";
    cout << num[2];

    return 0;
}
