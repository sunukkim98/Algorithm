

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;

    cin >> N;

    if (N == 1) 
        return 0;
    
    int i = 2;
    while (N > 1) {
        if (N % i == 0) {
            N = N / i;
            cout << i << "\n";
        }else {
            i++;
        }
    }

    return 0;
}