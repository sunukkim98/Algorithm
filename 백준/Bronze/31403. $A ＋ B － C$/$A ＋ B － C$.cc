#include <iostream>
#include <string>

using namespace std;

string char_a, char_b, char_c;
int num_a, num_b, num_c;

int main() {

    cin >> char_a >> char_b >> char_c;

    num_a = stoi(char_a);
    num_b = stoi(char_b);
    num_c = stoi(char_c);

    int sum_of_string = stoi(char_a + char_b);

    cout << (num_a + num_b) - num_c << "\n";
    cout << sum_of_string - stoi(char_c) << "\n";

    return 0;
}
