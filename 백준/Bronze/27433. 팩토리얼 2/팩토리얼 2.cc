

#include <iostream>

using namespace std;

int N;

long long result = 1;

int main() {
    cin >> N;

    for (int i = 1; i <= N; i++) {
        result *= i;
    }

    cout << result;

    return 0;
}
