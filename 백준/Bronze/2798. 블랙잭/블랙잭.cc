

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    int card [100] = {0,};
    int sum = 0;

    for (int i = 0; i < N; i++) {
        cin >> card[i];
    }

    for (int i = 0; i < N-2; i++) {
        for (int j = i + 1; j < N; j++) {
            for (int k = j + 1; k < N; k++) {
                // cout << card[i] << " " << card[j] << " " << card[k] << "\n";
                if (card[i] + card[j] + card[k] <= M) {
                      if (sum < card[i] + card[j] + card[k]) {
                          // cout << card[i] << " " << card[j] << " " << card[k] << "\n";
                          sum = card[i] + card[j] + card[k];
                          // cout << sum << "\n";
                      }
                }
            }
        }
    }

    cout << sum;

    return 0;
}
