

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int arr[1001];

    for (int i = 0; i < 1001; i++) {
        arr[i] = -1001;
    }

    int N;
    cin >> N;

    int num = -1;

    for (int i = 0; i < N; i++) {
        cin >> num;
        arr[i] = num;
    }

    sort(arr, arr+1000);

    for (int i = 0; i < 1001; i++) {
        if (arr[i] > -1001) {
            cout << arr[i] << "\n";
        }
    }


    return 0;
}
