#include <iostream>

using namespace std;

int correct_chess [6] = {1,1,2,2,2,8};
int input_chess [7];

int main() {
    for (int i = 0; i < 6; i++) {
        cin >> input_chess[i];
        correct_chess[i] -= input_chess[i];
    }

    for (int i=0; i < 6; i++) {
        cout << correct_chess[i] << " ";
    }

    return 0;
}
