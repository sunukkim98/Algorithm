

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

    int N, M; cin >> N >> M;
    map<string, int> not_heard;
    map<string, int> not_seen;

    string name;
    for (int i = 0; i < N; i++) {
        cin >> name;
        not_heard.insert({name, i});
    }

    for (int i = 0; i < M; i++) {
        cin >> name;
        not_seen.insert({name, i});
    }

    int cnt = 0;

    for (const auto& iter:not_heard) {
        if (not_seen.find(iter.first) != not_seen.end()) {
            cnt++;
        }
    }
    cout << cnt << "\n";

    for (const auto& iter:not_heard) {
        if (not_seen.find(iter.first) != not_seen.end()) {
            cout << iter.first << "\n";
        }
    }

    return 0;
}
