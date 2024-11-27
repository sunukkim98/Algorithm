
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
    cout.tie(nullptr);
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int A_n, B_n; cin >> A_n >> B_n;
    unordered_map<int, bool> map;

    int element;
    for (int i = 0; i < A_n + B_n; i++) {
        cin >> element;
        if (map[element] == true) // 이미 존재한다면 map에서 제거
            map.erase(element);
        else // 존재하지 않는다면 추가한다.
            map[element] = true;
    }
    cout << map.size(); // 남은 map 사이즈를 출력

    return 0;
}
