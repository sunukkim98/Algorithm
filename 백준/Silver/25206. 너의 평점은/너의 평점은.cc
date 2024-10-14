// 필요한 변수: 과목명(string), 학점(float), 등급 저장(string), 전공과목별 합(float), 학점의 총합(int)
// 20번의 반복문이 반복된다
// 반복문:
//     과목명, 학점, 등급을 입력받는다.
//     과목의 등급이 P라면 전공과목별 합에 저장하지 않는다.
//     이외의 경우 전공과목별 합에 추가
//
// 학점의 총합에서 등급이 P인 항목의 학점을 뺀다.
// 전공과목별 합 / 학점의 총합 = 결과


#include <iostream>
#include <string>

using namespace std;

string course[20] = {"",};
float credit[20] = {};
string grade[20] = {""};
float sum_of_grade = 0.0;
float sum_of_credit = 0.0;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int i = 0; i < 20; i++) {
        cin >> course[i] >> credit[i] >> grade[i];

        if (grade[i].compare("P") == 0) {

        }else {
            if (grade[i].compare("A+") == 0) {
                sum_of_grade += credit[i] * 4.5;
            }else if (grade[i].compare("A0") == 0) {
                sum_of_grade += credit[i] * 4.0;
            }else if (grade[i].compare("B+") == 0) {
                sum_of_grade += credit[i] * 3.5;
            }else if (grade[i].compare("B0") == 0) {
                sum_of_grade += credit[i] * 3.0;
            }else if (grade[i].compare("C+") == 0) {
                sum_of_grade += credit[i] * 2.5;
            }else if (grade[i].compare("C0") == 0) {
                sum_of_grade += credit[i] * 2.0;
            }else if (grade[i].compare("D+") == 0) {
                sum_of_grade += credit[i] * 1.5;
            }else if (grade[i].compare("D0") == 0) {
                sum_of_grade += credit[i] * 1.0;
            }else if (grade[i].compare("F") == 0) {
                sum_of_grade += credit[i] * 0.0;
            }
        }

        if (grade[i].compare("P") != 0) {
            sum_of_credit += credit[i];
        }
    }

    float result = sum_of_grade / sum_of_credit;

    cout << fixed;
    cout.precision(6);
    cout << result;

    return 0;
}

