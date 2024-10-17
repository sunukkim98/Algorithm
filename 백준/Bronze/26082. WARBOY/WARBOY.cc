

#include <iostream>
#include <string>

using namespace std;

int A, B, C;

int main() {
    cin >> A >> B >> C;
    int rival_performance = B / A;

    int warboy_performance = rival_performance*3;

    cout << warboy_performance * C;

    return 0;
}
