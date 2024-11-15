

#include <iostream>


using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int arr[10000] = {0,};
    int num;

    for (int i = 0; i < N; i++) {
        cin >> num;
        arr[num-1]++;
    }

    for(int i = 0; i < 10000; i++) {
        if (arr[i] != 0) {
            for (int j = 0; j < arr[i]; j++) {
                cout << i + 1 << "\n";
            }
        }
    }

    return 0;
}
