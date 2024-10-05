#include <iostream>

using namespace std;


string slogan[4] = {"SONGDO", "CODE", "2023", "ALGORITHM"};
string cheering[4] = {"HIGHSCHOOL", "MASTER", "0611", "CONTEST"};
string input, output;
int main() {

    cin >> input;
    for (int i = 0; i < 4; i++) {
        if (input == slogan[i]) {
            output = cheering[i];
        }
    }
    cout << output;
    return 0;
}
