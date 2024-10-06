#include <iostream>

using namespace std;

string A, B;

int main() {
    cin >> A >> B;

    char temp = A[0];
    A[0] = A[2];
    A[2] = temp;

    temp = B[0];
    B[0] = B[2];
    B[2] = temp;

    if (stoi(A) > stoi(B)) {
        cout << A;
    }else {
        cout << B;
    }

    return 0;
}
