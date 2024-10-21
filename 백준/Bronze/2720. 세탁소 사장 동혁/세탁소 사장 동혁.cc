// 반복할 횟수를 입력받는다. T(int형 변수)변수
// 거스름돈의 금액을 입력받는다. C(int형 변수)
// 2차원 배열 선언한다. change(int [T][4])
// C가 25보다 같거나 클 동안 반복한다. 반복 횟수마다 change[i][0]++
// 10보다 클 동안 반복 반복 횟수마다 change[i][1]++
// 5보다 클 동안 반복. 반복 횟수마다 change[i][2]++
// 0보다 클 동안 반복. 반복 횟수마다 change[i][3]++
//
// 최종적으로 change 2차원 배열을 출력한다.

#include <iostream>
#include <vector>
using namespace std;

int T = 0, C = 0;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> T;

    // 동적 배열 할당 (vector 사용)
    vector<vector<int>> change(T, vector<int>(4, 0));

    for (int i = 0; i < T; i++) {
        cin >> C;

        // 25센트 동전 계산
        while (C >= 25) {
            change[i][0]++;
            C -= 25;
        }

        // 10센트 동전 계산
        while (C >= 10) {
            change[i][1]++;
            C -= 10;
        }

        // 5센트 동전 계산
        while (C >= 5) {
            change[i][2]++;
            C -= 5;
        }

        // 1센트 동전 계산
        while (C > 0) {
            change[i][3]++;
            C -= 1;
        }
    }

    // 결과 출력
    for (int i = 0; i < T; i++) {
        cout << change[i][0] << " " << change[i][1] << " " << change[i][2] << " " << change[i][3] << '\n';
    }

    return 0;
}
