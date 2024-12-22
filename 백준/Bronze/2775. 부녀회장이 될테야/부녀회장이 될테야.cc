// k = 1, n = 3
// k층의 3번째 방에 사는 사람들의 수: 6
// 1명 2명 3명
// 6명
//
// i-1층에 사는 모든 방의 사람들의 수 합

// 1 2 3
// 1 3 6
// 1 4 10
// 1 5 15
// 1 6 21


#include <iostream>

using namespace std;

int get_num_of_people(int k, int n) {
    if (n == 1) {
        return 1;
    } else if (k == 0) {
        return n;
    } else {
        return (get_num_of_people(k - 1, n) + get_num_of_people(k, n - 1));
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;

    int k, n;
    int num_of_people = 1;
    for (int i = 0; i < t; i++) {
        cin >> k >> n;
        cout << get_num_of_people(k,n) << "\n";
    }


    return 0;
}