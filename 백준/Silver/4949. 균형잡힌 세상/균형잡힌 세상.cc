#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    while (true) {
        string line = "";
        stack<char> st;
        getline(cin, line);
        bool result = true;

        if (line.length() == 1 && line[0] == '.') {
            break;
        }

        for (int i = 0; i < line.length(); i++) {
            if (line[i] == '[' || line[i] == '(') {
                st.push(line[i]);
            }

            if (line[i] == ']') {
                if (!st.empty() && st.top() == '[') {
                    st.pop();
                } else {
                    result = false;
                    break;
                }
            } else if (line[i] == ')') {
                if (!st.empty() && st.top() == '(') {
                    st.pop();
                } else {
                    result = false;
                    break;
                }
            }
        }

        if (st.empty() && result) {
            cout << "yes\n";
        }else {
            cout << "no\n";
        }
    }

    return 0;
}