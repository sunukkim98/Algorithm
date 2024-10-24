

#include <iostream>

using namespace std;

int X;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int line = 1;
    cin >> X;

    //X가 위치한 대각선 찾기
    while(X - line > 0) {
        X -= line;
        line ++;
    }

    //대각선 홀수일 때
    if (line % 2) cout << line + 1 - X << '/' << X;
    //대각선 짝수일 때
    else cout << X << '/' << line + 1 - X;

    return 0;
}
