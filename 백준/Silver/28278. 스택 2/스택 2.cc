
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

    stack<int> stack;

    int n;
    cin >> n;
    int op_code;
    int x;
    for (int i = 0; i < n; i++) {
        cin >> op_code;
        // 정수 x를 스택에 넣는다.
        if (op_code == 1) {
            cin >> x;
            stack.push(x);
        }

        // 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        else if (op_code == 2) {
            if (stack.empty()) {
                cout << -1 << "\n";
            }else {
                cout << stack.top() << "\n";
                stack.pop();
            }
        }

        // 스택에 들어있는 정수의 개수를 출력한다.
        else if (op_code == 3) {
            cout << stack.size() << "\n";
        }

        // 스택이 비어있으면 1, 아니면 0을 출력한다.
        else if (op_code == 4) {
            if (stack.empty())
                cout << 1 << "\n";
            else
                cout << 0 << "\n";
        }

        // 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        else if (op_code == 5) {
            if (stack.empty()) {
                cout << -1 << "\n";
            }else {
                cout << stack.top() << "\n";
            }
        }
    }

    return 0;
}
