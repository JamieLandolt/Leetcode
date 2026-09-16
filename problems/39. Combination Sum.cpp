class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<vector<int>>> combs(target + 1, vector<vector<int>>{});
        combs.at(0).push_back(vector<int>{});

        for (int n = 1; n < target + 1; n++) {
            for (int num : candidates) {
                int prev = n - num;
                if (prev >= 0) {
                    for (vector<int> prev_comps : combs.at(prev)) {
                        if (prev_comps.size() > 0 && num >= prev_comps[prev_comps.size() - 1]) {
                            vector<int> n_comps(prev_comps);
                            n_comps.push_back(num);
                            combs.at(n).push_back(n_comps);
                        } else if (prev_comps.size() == 0) {
                            vector<int> n_comps(prev_comps);
                            n_comps.push_back(num);
                            combs.at(n).push_back(n_comps);
                        }
                    }
                }
            }
        }

        return combs.at(target);
    }
};
