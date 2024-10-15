

#include <iostream>
#include <string>

using namespace std;

int N, M;

int main() {
    cin >> N >> M;
    // cout << N << " " << M << endl;

    int A[N][M];
    int B[N][M];

    for (int i = 0; i < N; i++) {
        // cout << "loop1-1\n";
        for (int j = 0; j < M; j++) {
            // cout << "loop1-2\n";
            cin >> A[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> B[i][j];
        }
    }

    int result[N][M];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            result[i][j] = A[i][j] + B[i][j];
            cout << result[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}
