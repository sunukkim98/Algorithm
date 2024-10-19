#include <iostream>
#include <cmath>

using namespace std;

string N;
int B;

int main() {
    cin >> N >> B;

    int sum(0);

    for (int i = 0; i < N.length(); i++) {
        int temp = N[N.length() - (i + 1)];

        if ('0' <= temp && temp <= '9') {
            temp = temp - '0';
        } else {
            temp = temp + 10 - 'A';
        }
        sum += (temp * (int)pow(B, i));
    }

    cout << sum;
    return 0;
}
