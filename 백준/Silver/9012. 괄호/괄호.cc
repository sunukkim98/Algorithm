#include <iostream>
#include <string>
#include <stack>

using namespace std;

bool isBalanced(const string& line) {
    stack<char> stk;
    for (char c : line) {
        if (c == '(') {
            stk.push(c);
        } else if (c == ')') {
            if (stk.empty()) {
                return false; // 닫는 괄호가 여는 괄호보다 많음
            }
            stk.pop();
        }
    }
    return stk.empty(); // 스택이 비어 있어야 균형이 맞음
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t;
    cin >> t;
    string line;

    for (int i = 0; i < t; i++) {
        cin >> line;
        if (isBalanced(line)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}
