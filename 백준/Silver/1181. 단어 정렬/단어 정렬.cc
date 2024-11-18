

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(string a, string b) {
    if (a.length() != b.length()) {
        return a.length() < b.length();
    } else {
        return a < b;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    string words[20000];
    for (int i = 0; i < N; i++) {
        cin >> words[i];
    }
    sort(words, words+N, compare);
    string before = "";
    for (int i = 0; i < N; i++) {
        if (before == words[i]) continue;
        cout << words[i] << "\n";
        before = words[i];
    }

    return 0;
}
