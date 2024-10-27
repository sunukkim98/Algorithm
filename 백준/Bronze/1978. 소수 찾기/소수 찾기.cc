

#include <iostream>

using namespace std;

int N;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    int cnt = 0;
    int arr[100] = {0,};

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
        int divide[1000];
        int sum = 0;
        for (int j = 1; j <= arr[i]; j++) {
            if (arr[i] % j == 0) {
                sum += j;
                // cout << "sum: " <<sum << "\n";
            }
        }
        if (sum != 1) {
            if (sum == (arr[i] + 1)) {
                cnt++;
            }
        }
    }

    cout << cnt;

    return 0;
}
