class Solution {
public:
    bool predictTheWinner(vector<int>& nums) {
        vector<vector<vector<int>>> dp(
            nums.size() + 1, vector<vector<int>>(
                nums.size() + 1, vector<int>(2, 0)
            )
        );

        int player = 1 - nums.size() % 2;
        for (int i = 0; i < nums.size(); i++) {
            dp[i][i][player] = nums[i];
        }

        int base = player;
        int iters = nums.size() - 1;
        int iter_count = 0;
        int last_r = 0;
        for (int l = nums.size() - 1; 0 <= l; l--) {
            for (int r = l + 1; r < nums.size(); r++) {
                player = base ^ (l + r) % 2;

                int left = dp[l + 1][r][player] + nums[l];
                int right = dp[l][r - 1][player] + nums[r];
                
                if (left > right) {
                    dp[l][r][player] = left;
                    dp[l][r][1 - player] = dp[l + 1][r][1 - player];
                } else {
                    dp[l][r][player] = right;
                    dp[l][r][1 - player] = dp[l][r - 1][1 - player];
                }

            }
        }

        for (int l = 0; l < nums.size(); l++) {
            for (int r = 0; r < nums.size(); r++) {
                cout << setw(3) << dp[l][r][0] << "," << setw(3) << dp[l][r][1] << " ";
            }
            cout << "\n";
        }

        vector<int> vals = dp[0][nums.size() - 1];
        return vals[0] >= vals[1];
    }
};
