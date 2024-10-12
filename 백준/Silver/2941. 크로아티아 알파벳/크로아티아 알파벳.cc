// 0~5
// 01 12 23 34 45 56 67 78
// lj je es s= =n nj ja ak

#include <iostream>
#include <string>

using namespace std;


string c_alphabet[8] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
string input = "";

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> input;

    int cnt = (int) input.length();

    for (int i = 0; i < (int)input.length(); i++) {
        for (int j = 0; j < 8; j ++) {
            if (input.substr(i,(int)c_alphabet[j].length()).compare(c_alphabet[j]) == 0) {
                cnt--;
            }
        }
    }

    cout << cnt;

    return 0;
}

