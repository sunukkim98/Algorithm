#include <iostream>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    map<string,string> m;
    m.insert(pair<string,string>("Algorithm","204"));
    m.insert(pair<string,string>("DataAnalysis","207"));
    m.insert(pair<string,string>("ArtificialIntelligence","302"));
    m.insert(pair<string,string>("CyberSecurity","B101"));
    m.insert(pair<string,string>("Network","303"));
    m.insert(pair<string,string>("Startup","501"));
    m.insert(pair<string,string>("TestStrategy","105"));

    int n = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        cout << m[s] << "\n";
    }

    return 0;
}