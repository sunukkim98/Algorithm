#include <iostream>

using namespace std;

int R, S;
int total_cupcake;

int main() {
    cin >>  R >> S;
    total_cupcake = (R * 8) + (S * 3);
    cout << total_cupcake - 28;
    return 0;
}
