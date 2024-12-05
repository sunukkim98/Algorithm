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

    int n; cin >> n;

    int size[6] = {0,};
    for (int i = 0; i < 6; i++) {
        cin >> size[i];
    }
    // int s, m, l, xl, xxl, xxxl; cin >> s >> m >> l >> xl >> xxl >> xxxl;

    int t, p; cin >> t >> p;
    int t_cnt = 0;
    int p_bundle, p_num;

    for (int i = 0; i < 6; i++) {
        if (size[i] == 0) {
            continue;
        }
        if (size[i] <= t) {
            t_cnt++;
        }else {
            t_cnt += size[i] / t;
            if (size[i] % t != 0) {
                t_cnt++;
            }
        }
    }
    cout << t_cnt << "\n";

    p_bundle = n / p;
    p_num = n % p;
    cout << p_bundle << " " << p_num;
    return 0;
}
