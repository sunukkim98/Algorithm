// 테스트케이스 개수를 입력받는다.
// 테스트 케이스만큼 반복:
//     문서의 개수를 입력받는다.(1<= n <= 100)
//     몇 번째로 인쇄되었는지 궁금한 문서의 위치를 입력받는다.(0 <= m <= n)
//     N개 문서의 중요도가 차례대로 주어진다.(중요도는 1이상 9이하의 정수, 중복 허용)
//     주어진 문서의 위치의 문서가 몇 번째로 출력되는지 출력한다.

#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int test_case;
    cin >> test_case;
    for (int i = 0; i < test_case; i++) {
        int cnt = 0;
        int n;
        cin >> n;
        int m;
        cin >> m;
        queue<pair<int, int>> q;
        priority_queue<int> pq;
        for (int j = 0; j < n; j++) {
            int priority;
            cin >> priority;
            q.push({j, priority});
            pq.push(priority);
        }
        while (!q.empty()) {
            int q_idx = q.front().first;
            int q_priority = q.front().second;
            q.pop();
            if (pq.top() == q_priority) {
                pq.pop();
                cnt++;
                if (q_idx == m) {
                    cout << cnt << "\n";
                    break;
                }
            }
            else {
                q.push({q_idx, q_priority});
            }
        }
    }

    return 0;
}