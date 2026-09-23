class Solution {
public:
    char sep = '|';

    string encode(vector<string>& strs) {
        string ans;
        for (string& s : strs) {
            ans += to_string(s.size()) + sep + s;
        }
        return ans;
    }

    vector<string> decode(string s) {
        vector<string> ans;
        string len;
        string curr;

        int add_count = 0;
        for (char& c : s) {
            if (add_count > 0) {
                add_count -= 1;
                curr += c;
                continue;
            } 
            if (curr.size() > 0) {
                ans.push_back(curr);
                curr = "";
            }
            if (c == sep) {
                add_count = stoi(len);
                if (add_count == 0) {
                    ans.push_back("");
                }
                len = "";
            } else {
                len += c;
            }
        }
        if (curr.size()) {
            ans.push_back(curr);
        }
        return ans;
    }
};

