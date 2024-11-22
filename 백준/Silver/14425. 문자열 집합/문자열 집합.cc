#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    map<string,bool> strings;
    int N; int M; cin>>N>>M;
    int cnt = 0;

    string S;
    for (int i = 0; i < N; i++) {
        cin >> S;
        strings.insert(make_pair(S,true));
    }

    string str;
    for (int i = 0; i < M; i++) {
        cin >> str;
        if (strings[str]) cnt++;
    }

    cout << cnt;

    return 0;
}
