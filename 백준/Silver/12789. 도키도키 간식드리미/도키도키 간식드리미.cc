
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <vector>
#include <set>
#include<stack>

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

    int n, t, cnt = 1;
    stack<int> st;
    cin >> n;
    while (n--) {
        cin >> t;

        // 현재 순번과 일치하면 통과
        if (t == cnt) cnt++;

        // 아니면 stack에 대기
        else st.push(t);

        while (!st.empty() && st.top() == cnt) {
            //stack 맨 위가 현재 순번과 일치한다면 통과
            st.pop();
            cnt++;
        }
    }

    if (st.empty()) cout << "Nice";
    else cout << "Sad";

    return 0;
}
