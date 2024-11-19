

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

struct Member {
    int age;
    string name;
    int order;
};

bool compare(Member a, Member b) {
    if (a.age == b.age)
        return a.order < b.order;
    return a.age < b.age;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    Member member[100000];
    for (int i = 0; i < 100000; i++) {
        member[i].age = 201;
        member[i].name = "?";
    }

    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> member[i].age >> member[i].name;
        member[i].order = i;
    }

    sort(member, member+100000, compare);

    for (int i = 0; i < N; i++) {
        cout << member[i].age << " " << member[i].name << "\n";
    }

    return 0;
}
