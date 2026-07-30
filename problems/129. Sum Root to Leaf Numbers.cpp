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
    int sumNumbers(TreeNode* root) {
        // Returns reversed paths
        vector<vector<int>> paths = pathSums(root);
        int total = 0;

        for (vector<int> path : paths) {
            int num = 0;
            long place = 1;

            for (int digit : path) {
                num += digit * place;
                place *= 10;
            }
            cout << num << "\n";
            total += num;
        }
        return total;
    }

    vector<vector<int>> pathSums(TreeNode* root) {
        if (!root) {
            return vector<vector<int>>{};
        }
        if (!root->left && !root->right) {
            return vector<vector<int>>{{root->val}};
        }

        vector<vector<int>> paths;
        vector<vector<int>> l = pathSums(root->left);
        vector<vector<int>> r = pathSums(root->right);

        for (vector<int> path : l) {
            path.insert(path.end(), root->val);
            paths.push_back(path);
        }
        for (vector<int> path : r) {
            path.insert(path.end(), root->val);
            paths.push_back(path);
        }

        return paths;
    }
};
