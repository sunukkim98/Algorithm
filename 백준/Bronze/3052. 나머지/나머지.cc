#include <iostream>
#include <unordered_set>

using namespace std;

int num_arr[10];
int val;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int count[42] = {0,};
    int result = 0;

    for (int i=0; i<10; i++) {
        cin >> val;
        num_arr[i] = val % 42;
    }

    for (int i = 0; i < 10; i++) {
        count[num_arr[i]]++;
    }
    for (int i = 0; i < 42; i++) {
        if (count[i] > 0) {
            result++;
        }
    }
    cout << result;

    return 0;
}
