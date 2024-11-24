#include <iostream>
#include <map>
#include <vector>
#include <cctype>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    map<string,int> key_name;
    map<int, string> key_int;

    int N, M; cin >> N >> M;
    string name;
    for (int i = 0; i < N; i++) {
        cin >> name;
        key_name.insert({name, i+1});
        key_int.insert({i+1, name});
    }

    string query;
    int num_query;
    for (int i = 0; i < M; i++) {
        cin >> query;
        // cout << "query : " << query << "\n";
        if (isdigit(query[0])) {
            num_query = stoi(query);
            // cout << "query : " << query << "\t num_query : " << num_query << "\n";
            cout << key_int[num_query] << "\n";
        }else {
            // cout << "query : " << query << "\n";
            cout << key_name[query] << "\n";
        }
    }

    return 0;
}
