
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    char A[50000], B[50000];
    cin >> A >> B;

    int result[100000];

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            int temp = (A[N-1-j]-'0') * (B[M-1-i]-'0');
            result[N+M-1-i-j] += temp;
        }
    }

    for (int i = N + M - 1; i > 0; i--) {
        result[i-1] += result[i] / 10;
        result[i] %= 10;
    }

    bool flag = false;
    for (int i = 0; i < N + M; i++) {
        if (!flag) {
            if (result[i] != 0)
                flag = true;
            else if (i == N + M - 1)
                cout << "0";
        }
        if (flag)
            cout << result[i];
    }

    return 0;
}

