

#include <iostream>

using namespace std;

int main() {
    int num;
    int paper[101][101] = {0,};
    int area=0;
    cin >> num;
    for (int i = 0; i < num; i++) {
        int width_s, height_s;
        cin >> width_s >> height_s;
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < 10; k++) {
                paper[width_s+j][height_s+k] = 1;
            }
        }
    }

    for (int i = 0; i < 101; i++) {
        for (int j = 0; j < 101; j++) {
            area += paper[i][j];
        }
    }

    cout << area;

    return 0;
}
