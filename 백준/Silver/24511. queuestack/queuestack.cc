
#include <iostream>
#include <deque>

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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;

    deque<int> dq;

    bool data_type[100001];
    for (int i = 0; i < n; i++) {
        cin >> data_type[i];
    }

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        //queue일때만 deque에 원소 삽입
        if (data_type[i] == 0) {
            dq.push_back(x);
        }
    }

    int m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;

        // stack일 경우 입력된 숫자가 pop되기 때문에 미리 dq에 넣는 과정 생략
        dq.push_front(x);
        
        cout << dq.back() << " ";
        dq.pop_back();
    }

    return 0;
}
