

#include <iostream>
#include <algorithm>


using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int arr[1000000];
    for (int i = 0; i < 1000000; i++) {
        arr[i] = 1000001;
    }
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr, arr+1000000);

    for (int i = 0; i < N; i++) {
        cout << arr[i] << "\n";
    }

    return 0;
}
