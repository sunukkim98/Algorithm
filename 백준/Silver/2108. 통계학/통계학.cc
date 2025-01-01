// 수의 개수 n을 입력받는다. (1 <= n <= 500000) n은 홀수

// n번의 반복:
//     정수를 입력받아 정수들에 저장한다. 입력되는 정수의 절댓값은 4000을 안넘김
// 산술평균을 구한다
//     n개의 수들의 합을 n으로 나눈값
// 중앙값을 구한다
//     n개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
// 최빈값을 구한다
//     n개의 수들 중 가장 많이 나타나는 값. 여러개 있을 경우 최빈값 중 두 번째로 작은 값.
// 범위를 구한다
//     n개의 수들 중 최댓값과 최솟값의 차이


#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

bool compare(pair<int, int> x, pair<int, int> y) {
    return x.second > y.second;
}

vector<int> arr;

int main () {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, tmp, range, mid = 0, most_val, mean = 0;
    int most = -9999;
    int num[8001] = {0,};
    bool not_first = false;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        arr.push_back(tmp);
        mean += tmp;
        num[tmp+4000]++;
    }
    sort(arr.begin(), arr.end());
    for (int i = 0; i < 8001; i++) {
        if (num[i] == 0)
            continue;
        if (num[i] == most) {
            if (not_first) {
                most_val = i - 4000;
                not_first = false;
            }
        }
        if (num[i] > most) {
            most = num[i];
            most_val = i - 4000;
            not_first = true;
        }
    }
    mid = arr[arr.size() / 2];
    mean = round((double)mean / n);
    range = arr.back() - arr.front();
    cout << mean << '\n' << mid << '\n' << most_val << '\n' << range;

    return 0;
}