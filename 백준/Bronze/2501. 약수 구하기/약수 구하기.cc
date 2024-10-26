

#include <iostream>

using namespace std;

int N, K;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> K;

    int arr[10000] = {0,};
    int cnt = 0;

    for (int i = 1; i <= N; i++) {
        if (N % i == 0) {
            arr[cnt] = i;
            cnt++;
        }
    }

    // if (cnt >= K) {
    //     cout << arr[K - 1];
    // }else {
    //     cout << 0;
    // }
    cout << arr[K - 1];

    return 0;
}