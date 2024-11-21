#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    map<int, bool> integers;

    int N; cin>>N;
    for (int i = 0; i < N; i++) {
        int card_num; cin>>card_num;
        integers.insert({card_num, true});
    }

    int M; cin>>M;
    for (int i = 0; i < M; i++) {
        int integer; cin>>integer;
        if (integers[integer])
            cout << true << " ";
        else
            cout << false << " ";
    }

    return 0;
}
