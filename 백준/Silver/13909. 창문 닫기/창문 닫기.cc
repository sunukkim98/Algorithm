
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <vector>
#include <set>

using namespace std;

int GCD(int x, int y) {
    if (y == 0)
        return x;
    return GCD(y, x % y);
}

bool check_prime(long long n) {
    if (n <= 1) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i++) {
        if (n % i == 0 || n % (i + 2) == 0){
            return false;
        }
    }
    return true;
}

bool compare(int x, int y) {
    return y < x;
}

const int Max = 2100000000;

int main() {
    /*
     * 문제 개념
     * N번 째 창문이 열려 있으려면, 열고 닫은 횟수가 홀수번
     * 따라서, N의 약수의 개수가 홀수
     * 이런 특성을 만족하는 것은 제곱수
     * - 약수는 두 수가 짝을 이루어 곱해지므로 자연수의 약수의 개수는 짝수이지만, 제곱수는 자기 자신을 곱하는 수가 추가되므로 홀수
     * 따라서 주어진 범위 내의 제곱수의 개수를 구하면 문제를 해결 가능.
     */
    cout.tie(nullptr);
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int n, cnt = 0;
    cin >> n;

    for (int i = 1; i * i <= n; i++)
        cnt++;
    cout << cnt;
    return 0;
}
