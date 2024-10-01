//A와 B를 입력받는다.
//(A+B)*(A-B)를 출력한다.

#include <iostream>

using namespace std;

long long A, B;

int main() {
    cin >> A >> B;

    cout << (A + B) * (A - B);

    return 0;
}