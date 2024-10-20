#include <iostream>
#include <cmath>

using namespace std;

int N, B;
string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int main() {
    cin >> N >> B;

    string N_digit_num;

    while(N >= B) {
        string temp = to_string(N % B);
        N /= B;
        if (0 <= stoi(temp) && stoi(temp) <= 9) {

        }else {
            temp = alpha[stoi(temp) - 10];
        }
        N_digit_num.insert(0, temp);
    }

    string temp2 = to_string(N);
    if (0 <= N && N <= 9) {
        N_digit_num.insert(0, to_string(N));
    }else {
        temp2 = alpha[N - 10];
        N_digit_num.insert(0, temp2);
    }

    cout << N_digit_num;
    return 0;
}
