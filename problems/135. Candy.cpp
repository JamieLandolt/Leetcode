class Solution {
public:
    int candy(vector<int>& ratings) {
        map<int, vector<int>> positions;
        for (int i = 0; i < ratings.size(); i++) {
            positions[ratings.at(i)].push_back(i);
        }

        vector<int> ans(ratings.size(), -1);
        for (const auto& [_, v] : positions) {
            for (int pos : v) {
                int most_adj_candies = get_max(ratings, ans, pos);
                if (most_adj_candies == -1) {
                    ans[pos] = 1;
                } else {
                    ans[pos] = most_adj_candies + 1;
                }
            }
        }

        return accumulate(ans.begin(), ans.end(), 0);
    }   

    int get_max(vector<int>& ratings, vector<int>& ans, int& pos) {
        if (pos == 0) {
            if (ans.size() == 1) {
                return -1;
            }
            return ans[1];
        }
        int prev_ix = pos - 1;
        int prev_num = ratings[prev_ix];
        int curr_num = ratings[pos];
        if (pos == ans.size() - 1) {
            if (prev_num == curr_num) {
                return 0;
            }
            return ans[prev_ix];
        }
        int next_num = ratings[pos + 1];

        if (prev_num == curr_num) {
            if (next_num >= curr_num) {
                return 0;
            } else {
                return ans[pos + 1];
            }
        } else if (curr_num == next_num) {
            if (prev_num >= curr_num) {
                return 0;
            } else {
                return ans[pos - 1];
            }
        }

        return max(ans[pos - 1], ans[pos + 1]);
    }

};
