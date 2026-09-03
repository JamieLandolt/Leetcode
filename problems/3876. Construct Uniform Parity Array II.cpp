#include <algorithm>

class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        if (*min_element(nums1.begin(), nums1.end()) % 2 == 0) {
            for (int i = 0; i < nums1.size(); i++) {
                if (nums1[i] % 2 == 1) {
                    return false;           
                }
            }
        }
        return true;
    }
};
