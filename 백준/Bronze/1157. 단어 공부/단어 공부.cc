
// 각 알파벳에 대응되는 순서대로 단어크기만큼 반복하며 체크해 배열에 저장한다.


#include <iostream>
#include <string>

using namespace std;

using namespace std;

string word;

int main() {
    cin >> word;

    int num_of_alphabet [26];

    for (int i = 0; i < 26; i++) {
        num_of_alphabet[i] = 0;
    }

    for (int i = 0; i < word.length(); i++) {
        if (word[i] == 'A' || word[i] == 'a') {
            num_of_alphabet[0]++;
        }else if (word[i] == 'B' || word[i] == 'b') {
            num_of_alphabet[1]++;
        }else if (word[i] == 'C' || word[i] == 'c') {
            num_of_alphabet[2]++;
        }else if (word[i] == 'D' || word[i] == 'd') {
            num_of_alphabet[3]++;
        }else if (word[i] == 'E' || word[i] == 'e') {
            num_of_alphabet[4]++;
        }else if (word[i] == 'F' || word[i] == 'f') {
            num_of_alphabet[5]++;
        }else if (word[i] == 'G' || word[i] == 'g') {
            num_of_alphabet[6]++;
        }else if (word[i] == 'H' || word[i] == 'h') {
            num_of_alphabet[7]++;
        }else if (word[i] == 'I' || word[i] == 'i') {
            num_of_alphabet[8]++;
        }else if (word[i] == 'J' || word[i] == 'j') {
            num_of_alphabet[9]++;
        }else if (word[i] == 'K' || word[i] == 'k') {
            num_of_alphabet[10]++;
        }else if (word[i] == 'L' || word[i] == 'l') {
            num_of_alphabet[11]++;
        }else if (word[i] == 'M' || word[i] == 'm') {
            num_of_alphabet[12]++;
        }else if (word[i] == 'N' || word[i] == 'n') {
            num_of_alphabet[13]++;
        }else if (word[i] == 'O' || word[i] == 'o') {
            num_of_alphabet[14]++;
        }else if (word[i] == 'P' || word[i] == 'p') {
            num_of_alphabet[15]++;
        }else if (word[i] == 'Q' || word[i] == 'q') {
            num_of_alphabet[16]++;
        }else if (word[i] == 'R' || word[i] == 'r') {
            num_of_alphabet[17]++;
        }else if (word[i] == 'S' || word[i] == 's') {
            num_of_alphabet[18]++;
        }else if (word[i] == 'T' || word[i] == 't') {
            num_of_alphabet[19]++;
        }else if (word[i] == 'U' || word[i] == 'u') {
            num_of_alphabet[20]++;
        }else if (word[i] == 'V' || word[i] == 'v') {
            num_of_alphabet[21]++;
        }else if (word[i] == 'W' || word[i] == 'w') {
            num_of_alphabet[22]++;
        }else if (word[i] == 'X' || word[i] == 'x') {
            num_of_alphabet[23]++;
        }else if (word[i] == 'Y' || word[i] == 'y') {
            num_of_alphabet[24]++;
        }else if (word[i] == 'Z' || word[i] == 'z') {
            num_of_alphabet[25]++;
        }
    }

    char alphabet[26] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};

    int temp = num_of_alphabet[0];
    int index = 0;
    for (int i = 1; i < 26; i++) {
        if (num_of_alphabet[i] > temp) {
            temp = num_of_alphabet[i];
            index = i;
        }
    }

    for (int i = 0; i < 26; i++) {
        if (i != index) {
            if (num_of_alphabet[index] == num_of_alphabet[i]) {
                cout << '?';
                return 0;
            }
        }
    }

    cout << alphabet[index];

    return 0;
}
