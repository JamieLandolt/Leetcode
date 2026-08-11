#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

vector<string> split(string line, char sep) {
    vector<string> res;
    string s;
    for (char c : line) {
        if (c == sep && s.size() != 0) {
            res.push_back(s);
            s = "";
        } else if (c != sep) {
            s += c;
        }
    }

    if (s.size() != 0) {
        res.push_back(s);
    }
    return res;
}

int main() {
    vector<vector<string>> ans;
    ifstream file("file.txt");
    string line;

    while (getline(file, line)) {
        vector<string> parts = split(line, ' ');
        for (int i = 0; i < parts.size(); i++) {
            if (ans.size() < parts.size()) {
                ans.push_back(vector<string>{});
            }
            ans.at(i).push_back(parts.at(i));
        }
    }

    for (int row = 0; row < ans.size(); row++) {
        for (int col = 0; col < ans.at(row).size(); col++) {
            cout << ans.at(row).at(col);
            if (col == ans.at(row).size() - 1) {
                cout << '\n';
            } else {
                cout << ' ';
            }
        }
    }

    return 0;
}
