

#include <iostream>
#include <algorithm>

using namespace std;

struct Point {
    int x, y;
};

bool compare(const Point& p1, const Point& p2) {
    if (p1.x == p2.x)
        return p1.y < p2.y;
    return p1.x < p2.x;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    Point point[100000];
    for (int i = 0; i < 100000; i++) {
        point[i].x = 999999;
        point[i].y = 999999;
    }

    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> point[i].x >> point[i].y;
    }

    sort(point, point+100000, compare);

    for (int i = 0; i < N; i++) {
        cout << point[i].x << " " << point[i].y << "\n";
    }

    return 0;
}
