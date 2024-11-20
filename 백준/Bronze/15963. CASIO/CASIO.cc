#include <iostream>
#include <string>
#include <algorithm>
#include <utility>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, M;
    cin >> N >> M;

    bool result = false;
    if (N == M)
        result = true;

    cout << result;

    return 0;
}
