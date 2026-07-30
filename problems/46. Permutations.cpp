class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        if (nums.size() == 1) {
            return vector<vector<int>> {nums};
        }
        
        int elem = nums.at(0);
        nums.erase(nums.begin());
        vector<vector<int>> perms = permute(nums);
        vector<vector<int>> newPerms;
        
        for (vector<int> perm : perms) {
            for (int i = 0; i < perm.size() + 1; i++) {
                vector<int> newPerm(perm);
                newPerm.insert(newPerm.begin() + i, elem);
                newPerms.push_back(newPerm);
            }
        }

        return newPerms;
    }
};
