

#include <iostream>
#include <algorithm>


using namespace std;

bool compare(int a, int b) {
    return a > b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, k;
    cin >> N >> k;

    int arr[1000];
    for (int i = 0; i < 1000; i++) {
        arr[i] = -1;
    }
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr, arr+1000, compare);

    cout << arr[k-1];

    return 0;
}
