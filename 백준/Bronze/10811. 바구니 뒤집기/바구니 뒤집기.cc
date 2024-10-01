#include <iostream>

using namespace std;

int N,M;
int flip_start, flip_end;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    int basket[N];
    for (int i=0; i<N; i++) {
        basket[i] = i + 1;
    }

    int reverse_basket[N];
    for (int i=0; i<N; i++) {
        reverse_basket[i] = i + 1;
    }

    for (int i=0; i<M; i++) {
        cin >> flip_start >> flip_end;
        int cnt = flip_start-1;
        for (int j=flip_end-1; j >= flip_start-1; j--) {
            reverse_basket[cnt] = basket[j];
            cnt++;
        }

        for (int i=0; i<N; i++) {
            basket[i] = reverse_basket[i];
        }
    }

    for (int i=0; i<N; i++) {
        cout << basket[i] << " ";
    }
    cout << "\n";
    
    return 0;
}

// 1 2 3 4 5
// 2 1 3 4 5
// 2 1 4 3 5
// 3 4 1 2 5
// 3 4 1 2 5
//
// 새로운 배열을 만든다
// 새로운 배열에 입력으로 받은 두 범위를 거꾸로 저장한다.
// 값이 0인 경우만 해당 인덱스와 같은 기존 배열 값을 저장한다.
// 이를 출력한다.