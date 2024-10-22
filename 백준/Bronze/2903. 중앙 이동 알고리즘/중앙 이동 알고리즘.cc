// 초기 사각형의 길이를 2로 설정한다.
// 반복문을 N까지 반복한다.
//     반복문:
//     초기 사각형의 길이 = 초기 사각형 길이 + pow(2,i)가 결과 사각형의 길이이다.
// 초기 사강형의 길이 * 초기 사각형의 길이 출력

#include <iostream>
#include <cmath>

using namespace std;

int edge_length = 2, N;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    for (int i = 0; i < N; i++) {
        edge_length += pow(2,i);
    }

    cout << edge_length * edge_length;

    return 0;
}
