// i를 입력받는다.
// i가 3의 배수의 여부를 저장한다
// i가 5의 배수의 여부를 저장한다
// i가 3의 배수이면서 5의 배수이면 FizzBuzz를 출력
// i가 3의 배수이지만 5의 배수가 아니면 Fizz를 출력
// i가 3의 배수가 아니지만 5의 배수이면 Buzz를 출력
// i가 3의 배수도 아니고 5의 배수도 아닌 경우 i를 그대로 출력
//
// 3개의 문자열을 입력받는다.
// 문자열이 숫자인지 확인한다.
// 숫자라면 그 다음 숫자를 저장
// 다음 숫자가 3과 5로 나눠지는지 확인
// 위의 조건대로 출력


#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string input[3];
    for (int i = 0; i < 3; i++) {
        cin >> input[i];
    }

    int num[3];
    int next_num = 0;
    for (int i = 0; i < 3; i++) {
        try {
            num[i] = stoi(input[i]);
            // cout << num[i] << "\n";
            if (i == 0) {
                next_num = num[i] + 3;
                // cout << next_num << "\n";
            } else if (i == 1) {
                next_num = num[i] + 2;
                // cout << next_num << "\n";
            } else if (i == 2) {
                next_num = num[i] + 1;
                // cout << next_num << "\n";
            }
        } catch (invalid_argument e) {
            // cout << input[i] << "\n";
        }
    }

    bool flag1 = false, flag2 = false;

    if (next_num == 0) {
        cout << "Invalid Input" << endl;
    } else {
        if (next_num % 3 == 0) {
            flag1 = true;
        }
        if (next_num % 5 == 0) {
            flag2 = true;
        }
        if (flag1 && flag2) {
            cout << "FizzBuzz";
        } else if (flag1) {
            cout << "Fizz";
        } else if (flag2) {
            cout << "Buzz";
        } else {
            cout << next_num;
        }
    }

    return 0;
}