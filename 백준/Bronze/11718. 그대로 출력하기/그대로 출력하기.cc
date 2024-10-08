#include <iostream>
#include <string.h>

using namespace std;

string input[100];

int main() {
    int i=0;
    for (int i=0; i<100; i++) {
        getline(cin, input[i]);

        if (input[i] == "") {
            break;
        }
    }
    for (int i = 0; i < sizeof(input); i++) {
        cout << input[i] << "\n";
        if (input[i] == "") {
            break;
        }
    }

    return 0;
}
