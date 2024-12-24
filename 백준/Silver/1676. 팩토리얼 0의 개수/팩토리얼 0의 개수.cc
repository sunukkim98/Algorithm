// n을 입력받는다.
// n!을 구한다. 시간초과! -> 1부터 N까지 5와 2로 나누어 떨어지면 나누어 떨어지는 횟수 각각 저장
//
// n!이 10으로 나눈 나머지가 0이면 반복
//     구한 n!을 10으로 나눈 나머지 값이 0이면 카운트 1증가
//     n!을 10으로 나눈다.
// 카운트 출력

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    int exp_2 = 0, exp_5 = 0;
    int count_0 = 0;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        int temp = i;
        if (temp % 5 == 0) {
            while (temp % 5 == 0) {
                exp_5++;
                temp /= 5;
            }
        } else if (temp % 2 == 0) {
            while (temp % 2 == 0) {
                exp_2++;
                temp /= 2;
            }
        }
    }

    if (exp_2 < exp_5) {
        count_0 = exp_2;
    } else {
        count_0 = exp_5;
    }

    cout << count_0;

    return 0;
}