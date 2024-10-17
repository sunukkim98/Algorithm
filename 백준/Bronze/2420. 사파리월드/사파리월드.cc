

#include <iostream>
#include <string>

using namespace std;

long long N, M;

int main() {
    cin >> N >> M;

    if (N < M) {
        cout << -(N - M);
    }else {
        cout << N - M;
    }

    return 0;
}
