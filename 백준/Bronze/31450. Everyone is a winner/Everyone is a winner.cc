#include <iostream>

using namespace std;

long long M, K;

int main() {
    cin >> M >> K;
    if (M % K == 0) {
        cout << "Yes";
    }else {
        cout << "No";
    }
    return 0;
}
