// N을 입력받는다.(int)
// 시작 번호는 0이다.
// 1에 6의 i승을 더한다.
// 더한수가 N보다 크다면 반복을 멈춘다.
// i++
// i를 출력

#include <iostream>

using namespace std;

int N;
int start_num = 2;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    int i = 0;
    while (start_num <= N) {
        start_num += 6 * i;
        i++;
    }
    if (N == 1) i = 1;
    cout << i;

    return 0;
}
