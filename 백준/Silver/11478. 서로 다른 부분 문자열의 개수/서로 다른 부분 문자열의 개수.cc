
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

    string S; cin >> S;
    map<string, bool> subset;

    string str = "";
    for (int i = 0; i < S.size(); i++) {
        for (int j = i; j < S.size(); j++) {
            str += S[j];
            subset.insert({str, true});
        }
        str = "";
    }

    cout << subset.size();


    return 0;
}
