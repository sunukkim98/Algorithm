

#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
    cout.tie(nullptr);
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int N; cin >> N;
    vector<int> card_num(N);
    for (int i = 0; i < N; i++) {
        card_num.at(i) = 11111111;
    }

    int num;
    for (int i = 0; i < N; i++) {
        cin >> num;
        card_num.push_back(num);
    }

    sort(card_num.begin(), card_num.end());

    // for (int i = 0; i < N; i++) {
    //     cout << card_num.at(i) << "\n";
    // }

    int M; cin >> M;
    unordered_map<int, int> count_card;
    int card;
    vector<int> order;
    for (int i = 0; i < M; i++) {
        cin >> card;
        count_card.insert({card, 0});
        order.push_back(card);
    }

    for (int i = 0; i < N; i++) {
        if(count_card.find(card_num.at(i)) != count_card.end()) {
            count_card[card_num.at(i)]++;
        }
    }

    for (auto iter = order.begin(); iter != order.end(); ++iter) {
        cout << count_card[*iter] << " ";
    }

    return 0;
}
