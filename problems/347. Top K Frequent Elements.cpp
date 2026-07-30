class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        for (int num : nums) m[num]++;

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        for (const auto &[key, v] : m) {
            minHeap.push(pair<int, int>{v, key});
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }

        vector<int> v;
        while (!minHeap.empty()) {
            v.push_back(minHeap.top().second);
            minHeap.pop();
        }

        return v;
    }
};
