//for문으로 첫 입력으로 주어지는 T번 반복한다.
//for 문 안에서
//    반복할 숫자 R 과 문자열 S를 입력받는다.
//    문자열 P에 S의 자리수마다 R번 반복해 concat한다.
//    P를 출력한다.

#include <iostream>
#include <string>

using namespace std;
int T, R;
string S, P;
string str_arr[1000];

int main() {
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> R >> S;
        if ((!((R > 0) && (R < 9))) || ((S.length() < 1) && (S.length() > 20))) {
            break;
        }
        for (int j = 0; j < (int)S.length(); j++) {
            for (int k = 0; k < R; k++) {
                P = P + S[j];
            }
        }

        str_arr[i] = P;
        P = "";
    }


    for (int i = 0; i < T; i++) {
        cout << str_arr[i] << "\n";
    }

    return 0;
}