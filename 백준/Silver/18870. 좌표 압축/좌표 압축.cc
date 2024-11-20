

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    cout.tie(nullptr);
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    ///////////////////////////시간초과///////////////////////////
    // vector<int> x_points;
    // int cnt[1000000];
    //
    // int N;
    // cin >> N;
    //
    // int point;
    //
    // for (int i = 0; i < N; i++) {
    //     cin >> point;
    //     x_points.push_back(point);
    // }
    //
    // vector<int> temp = x_points;
    // sort(temp.begin(), temp.end());
    // temp.erase(unique(temp.begin(), temp.end()), temp.end());
    //
    // for (int i = 0; i < N; i++) {
    //     for (int j = 0; j < temp.size(); j++) {
    //         if (x_points[i] == temp[j]) {
    //             cnt[i] = j;
    //             break;
    //         }
    //     }
    // }
    //
    // for (int i = 0; i < N; i++) {
    //     cout << cnt[i] << " ";
    // }
    //////////////////////////////////////////////////////////

    int N;
    cin >> N;

    // 두개의 벡터를 사용시 시간초과를 해결하지 못함 pair를 사용해 idx를 같이 저장
    vector<pair<int, int>> num_idx_pairs(N);
    for (int i = 0; i < N; i++) {
        int input;
        cin >> input;

        num_idx_pairs[i] = {input, i};
    }

    sort(num_idx_pairs.begin(), num_idx_pairs.end());

    // 총 좌표중 자신의 좌표보다 작은 개수 저장할 벡터
    vector<int> count_vector(N);

    int prev = INT32_MAX;
    int count = -1;

    for (int i = 0; i < N; i++) {
        // 이전에 비교한 숫자와 같지 않다면 count 증가
        if (prev != num_idx_pairs[i].first)
            count++;

        // 해당 좌표보다 작은 개수를 저장할 벡터의 좌표 위치에 count값을 저장
        count_vector[num_idx_pairs[i].second] = count;

        // 이전에 비교한 좌표 업데이트
        prev = num_idx_pairs[i].first;
    }

    for (int i : count_vector) {
        cout << i << ' ';
    }

    return 0;
}
