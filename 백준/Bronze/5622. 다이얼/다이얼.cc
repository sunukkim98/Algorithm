#include <iostream>
#include <string.h>

using namespace std;

char alphabet [26] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
int score [26] = {3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10};
int main() {
    int output = 0;

    char input[16];

    cin >> input;

    for (int i = 0; i < strlen(input); i++) {
        for (int j = 0; j < strlen(alphabet); j++) {
            if (input[i] == alphabet[j]) {
                output += score[j];
            }
        }
    }

    cout << output;


    return 0;
}
