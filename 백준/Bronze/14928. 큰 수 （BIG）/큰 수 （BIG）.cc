
#include <iostream>
#include <string>

using namespace std;

string N;

int main() {
    cin >> N;
    int ans = 0;
    for (int i = 0; i < N.size(); i++) {
        ans = (ans * 10 + (N[i]-'0')) % 20000303;
    }
    cout << ans;

    return 0;
}