

#include <iostream>
#include <algorithm>

using namespace std;

bool compare(int a, int b) {
    return a > b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string N;
    cin >> N;
    int arr[N.length()];
    for (int i = 0; i < N.length(); i++) {
        arr[i] = N[i] - '0';
    }

    //내림차순 정렬
    sort(arr, arr+N.length(), compare);

    for (int i = 0; i < N.length(); i++) {
        cout << arr[i];
    }

    return 0;
}
