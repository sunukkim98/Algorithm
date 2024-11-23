#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int n; cin >> n;
    map<string,bool,std::greater<>> office_status;
    string name; string work_status;
    for (int i = 0; i < n; i++) {
        cin >> name >> work_status;
        if (work_status == "enter") {
            if (office_status[name] == false) {
                office_status[name] = true;
            }
            office_status.insert({name, true});
        }else if (work_status == "leave") {
            office_status[name] = false;
        }
    }

    for (auto iter = office_status.begin(); iter != office_status.end(); iter++) {
        if (iter->second == true) {
            cout << iter->first << "\n";
        }
    }

    return 0;
}
