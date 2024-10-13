
// 입력받을 단어의 개수를 N으로 입력받는다.
// N만큼 반복문을 반복할 것이다.
// 반복문:
//     단어를 입력받는다.
//     입력받은 단어의 길이만큼 반복문을 돌린다.
//     반복문2:
//         단어에 있는 각 문자를 배열에 저장해간다.
//         조건문:
//             만약 배열에 이미 있었고 그 전의 단어가 같은 문자가 아니라면 카운트하지 않는다.
//         조건문과 다른 경우:
//             카운트한다.
//
// 카운트 출력

#include <iostream>
#include <string>

using namespace std;

int N;
int cnt = 0;

int main() {
    cin >> N;
    for (int i = 0; i < N; i ++) {
        string word;
        cin >> word;

        bool alphabet[26] = {false, };
        alphabet[(int)word[0] - 97] = true;

        for (int j = 1; j < word.length(); j ++) {
            if (word[j] == word[j - 1]) {
                continue;
            }

            else if (word[j] != word[j - 1] && alphabet[(int)word[j] - 97] == true) {
                cnt++;
                break;
            }

            else {
                alphabet[(int)(word[j] - 97)] = true;
            }
        }
    }

    cout << N - cnt;

    return 0;
}
