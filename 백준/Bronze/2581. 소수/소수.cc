

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N;
    int sum = 0, min = -1;
    int cnt = 0;

    cin >> M >> N;

    for (int i = M; i <= N; i++) {
        for (int j = 1; j <= i; j++) {
            if (i % j == 0) {
                cnt++;
            }
        }
            if (cnt == 2) { // i가 소수일 때
                if (min == -1) {
                    min = i;
                }
                sum += i;
            }
            cnt = 0;
    }

    if (min == -1)
        cout << -1 << '\n';
    else
        cout << sum << '\n' << min << '\n';

    return 0;
}
