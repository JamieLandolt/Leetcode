class Solution {
public:
    bool closeStrings(string word1, string word2) {
        unordered_map<char, int> freq1;
        unordered_map<char, int> freq2;
        set<char> letters1;
        set<char> letters2;
        for (char c : word1) {
            freq1[c]++;  
            letters1.insert(c);
        } 
        for (char c : word2) {
            freq2[c]++;  
            letters2.insert(c);
        } 

        unordered_map<int, int> freq_1;
        unordered_map<int, int> freq_2;
        for (const auto& [_, v] : freq1) freq_1[v]++;
        for (const auto& [_, v] : freq2) freq_2[v]++;

        return freq_1 == freq_2 && letters1 == letters2;
    }
};
