
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <vector>
#include <set>

using namespace std;

int GCD(int x, int y) {
    if (y == 0)
        return x;
    return GCD(y, x % y);
}

int main() {
    cout.tie(nullptr);
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int n;
    cin >> n;
    vector<int> arr, distance;
    int num;

    for (int i = 0; i < n; i++) {
        cin >> num;
        arr.push_back(num);
    }

    for (int i = 1; i < n; i++) {
        distance.push_back(arr[i] - arr[i-1]);
    }

    int GCD_distance = distance[0];
    for (int i = 0; i < n - 1; i++) {
        GCD_distance = GCD(GCD_distance, distance[i]);
    }

    int result = 0;
    for (int i = 0; i < n - 1; i++) {
        result += (distance[i] / GCD_distance) - 1;
        // cout << i + 1 << "th result: " << result << "\n";
    }

    // cout << "final result: " << result;
    cout << result;

    return 0;
}
