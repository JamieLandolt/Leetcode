class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> dp = vector<vector<int>>(
            text1.size() + 1, vector<int>(text2.size() + 1, 0));

        for (int i = 1; i < text1.size() + 1; i++) {
            for (int j = 1; j < text2.size() + 1; j++) {
                if (text1[i - 1] == text2[j - 1]) {
                    int prev = dp[i - 1][j - 1];
                    dp[i][j] = prev + 1;
                } else {
                    int l = dp[i - 1][j];
                    int r = dp[i][j - 1];
                    dp[i][j] = l > r ? l : r;
                }
            }
        }

        return dp[text1.size()][text2.size()];
    }
};
