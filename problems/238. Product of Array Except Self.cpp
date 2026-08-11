class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> pre(nums.size(), 1);
        vector<int> post(nums.size(), 1);

        if (nums.size() == 0) {
            return nums;
        }
        if (nums.size() == 1) {
            return vector<int>{1};
        }

        for (int i = 1; i < nums.size(); i++) {
            pre[i] = pre[i - 1] * nums[i - 1];
        }

        for (int i = nums.size() - 2; i >= 0; i--) {
            post[i] = post[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < pre.size(); i++) {
            cout << pre[i] << "|" << post[i] << "\n";
        }
        
        vector<int> ans;
        ans.push_back(post[0]);
        for (int i = 1; i < nums.size() - 1; i++) {
            ans.push_back(pre[i] * post[i]);
        }
        ans.push_back(pre[nums.size() - 1]);
        return ans;
    }
};
