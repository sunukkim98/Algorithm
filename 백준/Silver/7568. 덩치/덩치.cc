// 전체 사람의 수를 입력받는다. 2 <= N <= 50
// 전체 사람의 수만큼 반복한다.
//     각 사람의 몸무게와 키를 입력받는다.
// 몸무게와 키를 비교해 각 사람의 등수를 정한다.
// 입력된 순서대로 등수를 출력한다.

#include <iostream>
#include <algorithm>

using namespace std;

bool compare(pair<int, int> x, pair<int, int> y) {
    if ((x.first > y.first) && (x.second > y.second)) {
        return true;
    }
    return false;
}

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(NULL);
//     cout.tie(NULL);
//
//     int n;
//     cin >> n;
//
//     pair<int, int> size[51];
//     pair<int, int> sorted_size[51];
//     for (int i = 0; i < 50; i++) {
//         size[i].first = 0;
//         size[i].second = 0;
//         sorted_size[i].first = 0;
//         sorted_size[i].second = 0;
//     }
//
//     for (int i = 0; i < n; i++) {
//         int x, y;
//         cin >> x >> y;
//         size[i] = make_pair(x, y);
//         sorted_size[i] = make_pair(x, y);
//     }
//
//
//     sort(sorted_size, sorted_size + 50, compare);
//
//     for (int i = 0; i < n; i++) {
//         cout << sorted_size[i].first << " " << sorted_size[i].second << "\n";
//     }
//
//     int ranking[51] = {0,};
//     int rank = 1;
//     int stack = 1;
//     ranking[0] = 1;
//     for (int i = 1; i < n; i++) {
//         if (sorted_size[i].first <= sorted_size[i - 1].first && sorted_size[i].second <= sorted_size[i - 1].second) {
//             rank += stack;
//             stack = 1;
//         }else {
//             stack++;
//         }
//         ranking[i] = rank;
//     }
//
//     for (int i = 0; i < n; i++) {
//         cout << ranking[i] << "\n";
//     }
//
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < n; j++) {
//             if (size[i].first == sorted_size[j].first && size[i].second == sorted_size[j].second) {
//                 cout << ranking[j] << " ";
//             }
//         }
//     }
//
//     return 0;
// }

int main() {
    int n;
    int x[51], y[51];
    int size[51] = {0, };

    cin >> n;

    for (int i = 1; i <= n; i++) {
        cin >> x[i] >> y[i];
    }

    // for (int i = 1; i <= n; i++) {
    //     cout << x[i] << " " << y[i] << "\n";
    // }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (x[i] < x[j] && y[i] < y[j]) {
                size[i]++;
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        cout << size[i] + 1 << " ";
    }

    return 0;
}