
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

    int T; cin >> T;
    int H, W, N;
    int result;

    for (int i = 0; i < T; i++) {
        cin >> H >> W >> N;

        if (N % H == 0) {
            result = H * 100 + (N / H);
        }else {
            result = (N % H) * 100 + (N / H) + 1;
        }
        cout << result << "\n";
    }

    return 0;
}
