// 9 * 9 2차원 배열을 선언한다.(int)
// 매 행마다 최댓값을 구한다.
// 열의 index도 함께 저장한다. 크기 9 배열(int) index+1
// 매 행의 최댓값 중 가장 큰 값을 구한다.
// 행의 index도 저장한다. index+1

#include <iostream>
#include <string>

using namespace std;

int matrix[9][9];

int main() {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> matrix[i][j];
        }
    }

    int temp = -1;
    int row_idx = -1, col_idx = -1;

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (temp < matrix[i][j]) {
                temp = matrix[i][j];
                row_idx = i;
                col_idx = j;
            }
        }
    }

    cout << temp << "\n" << row_idx + 1 << " " << col_idx + 1 << "\n";

    return 0;
}
