// 의견의 개수 n을 입력받는다. (0 <= n <= 3 * 10^5)
// n의 절사평균을 구하기 위해 n의 15%를 계산 후 반올림한다.
// n번 반복
//     의견을 입력받는다. (1 <= 의견 <= 30)
// 입력받은 의견을 정렬한다.
// 정렬된 의견들 중 상위 15% 하위 15%를 의견에서 제거한다.
// 나머지 의견들을 종합해 평균을 구한다. (소수점 자리는 반올림 처리)
// 해당 문제의 난이도를 출력한다.

#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main () {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;
    if (n == 0) {
        cout << 0;
        return 0;
    }
    double outlier_num = round(n * 0.15);
    int opinions[300001];
    for (int i = 0; i < 300001; i++) {
        opinions[i] = 99;
    }
    for (int i = 0; i < n; i++) {
        cin >> opinions[i];
    }
    sort(opinions, opinions+300001);
    for (int i = 0; i < outlier_num; i++) {
        opinions[i] = 99;
    }
    for (int i = n-1; i > n - outlier_num - 1; i--) {
        opinions[i] = 99;
    }
    sort(opinions, opinions+300001);
    // for (int i = 0; i < n; i++) {
    //     cout << opinions[i] << " ";
    // }
    // cout << "\n";
    double difficulty_level = 0;
    for (int i = 0; i < n - (outlier_num * 2); i++) {
        difficulty_level += opinions[i];
    }
    // cout << (n - (outlier_num * 2));
    cout << round((difficulty_level / (n - (outlier_num * 2))));

    return 0;
}