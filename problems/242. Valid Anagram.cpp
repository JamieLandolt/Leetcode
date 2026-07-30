class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> ms;
        unordered_map<char, int> mt;
        for (char& c : s) {
            ms[c]++;
        }
        for (char& c : t) {
            mt[c]++;
        }

        return ms == mt;
    }
};
