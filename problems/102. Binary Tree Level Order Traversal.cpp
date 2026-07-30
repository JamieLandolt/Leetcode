/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levels;
        get_levels(root, 0, levels);
        return levels;
    }

    void get_levels(TreeNode* root, int level, vector<vector<int>>& levels) {
        if (!root) {
            return;
        }
        if (levels.size() > level) {
            levels.at(level).push_back(root->val);
        } else {
            levels.push_back(vector<int>{root->val});
        }
        get_levels(root->left, level + 1, levels);
        get_levels(root->right, level + 1, levels);
        
    }
};
