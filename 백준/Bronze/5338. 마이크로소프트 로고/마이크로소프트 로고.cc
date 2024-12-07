/*
_.-;;-._
'-..-'|   ||   |
'-..-'|_.-;;-._|
'-..-'|   ||   |
'-..-'|_.-''-._|
 */
#include <iostream>
#include <map>
#include <vector>
#include <cctype>

using namespace std;

int GCD(int x, int y) {
    if (y == 0)
        return x;
    return GCD(y, x % y);
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cout << "       _.-;;-._" << "\n";
    cout << "'-..-'|   ||   |" << "\n";
    cout << "'-..-'|_.-;;-._|" << "\n";
    cout << "'-..-'|   ||   |" << "\n";
    cout << "'-..-'|_.-''-._|";
    return 0;
}
