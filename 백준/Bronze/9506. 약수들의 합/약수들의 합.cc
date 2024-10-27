// 우선 숫자가 주어졌을 때 그게 완전수인지 판별 할 수 있어야 한다. done.
// 입력이 -1이면 종료하는 무한 반복문을 반복한다.

#include <iostream>

using namespace std;

int N;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while(1) {
        cin >> N;
        int max = 0;
        if (N == -1) {
            break;
        }else {
            int divisor[100000] = {-1,};
            int sum = 0;

            for (int i = 1; i < N; i++) {
                if (N % i == 0) {
                    divisor[i] = i;
                    if (max < divisor[i]) {
                        max = divisor[i];
                    }
                }
                if (divisor[i] > 0) {
                    sum += divisor[i];
                }
            }

            if (sum == N) {
                cout << N << " = ";
                for (int i = 1; i < N; i++) {
                    if (divisor[i] > 0) {
                        if (divisor[i] == max) {
                            cout << divisor[i] << "\n";
                        }else {
                            cout << divisor[i] << " + ";
                        }
                    }
                }
            }else {
                cout << N << " is NOT perfect.\n";
            }
        }
    }

    return 0;
}
