class Solution {
public:
    string smallestPalindrome(string s) {
        if (s.size() == 1) {
            return s;
        }

        unordered_map<char, int> m;
        for (char& c : s) {
            if (m.count(c)) {
                m[c]++;
            } else {
                m[c] = 1;
            }
        }

        string c = "";
        for (const auto &[key, val] : m) {
            std::cout << key << ": " << val << "\n";
            if (val % 2 == 1) {
                c = key;
                break;
            }
        }

        string alphabet = "abcdefghijklmnopqrstuvwxyz";
        string first_half = "";
        string last_half = "";

        for (char& c : alphabet) {
            if (m.contains(c)) {
                int val = m.at(c) / 2;
                for (int i = 0; i < val; i++) {
                    first_half += c;
                    last_half += c;
                }
            }
        }

        reverse(last_half.begin(), last_half.end());
        return first_half + c + last_half;
    }
};
