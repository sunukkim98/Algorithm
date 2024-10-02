//시험 본 과목의 개수 N을 입력받는다.(N<=1000)
//입력받은 N만큼 for반복문이 동작한다.
//    반복문 안:
//        과목의 점수를 입력받는다.(score <= 100 && score > -1)
//        과목 점수 배열의 i번째 값에 점수를 저장
//점수 배열의 모든 점수를 0보다 큰 값이 있는지 확인한다. 이를 bool값으로 출력
//새로운 점수 배열에 기존 점수에 대해 새롭게 계산해 저장한다

#include <iostream>

using namespace std;

int N;
bool has_positive = false;

int main() {
    cin >> N;

    int score[N];

    for (int i = 0; i < N; i++) {
        cin >> score[i];
        if (score[i] > 0) {
            has_positive = true;
        }
    }

    if (!has_positive) {
        cout << "there is no score that is bigger than 0\n";
    }

    int M = score[0];

    for (int i = 1; i < N; i++) {
        if (M < score[i]) {
            M = score[i];
        }
    }

    int sum_of_new = 0;

    for (int i = 0; i < N; i++) {
        sum_of_new += score[i];
    }

    double result = sum_of_new * 100.0 / M / N;

    cout << result;

    return 0;
}