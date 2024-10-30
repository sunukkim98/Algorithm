

#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x[4];
    int y[4];

    for (int i = 0; i < 3; i++) {
        cin >> x[i] >> y[i];
    }

    // print x
    if(x[0] == x[1])
        cout << x[2] << " ";
    else if(x[0] == x[2])
        cout << x[1] << " ";
    else
        cout << x[0] << " ";

    // print y
    if(y[0] == y[1])
        cout << y[2];
    else if(y[0] == y[2])
        cout << y[1];
    else
        cout << y[0];

    return 0;
}