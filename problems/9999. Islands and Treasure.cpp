#include <queue>
class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int INF = exp(2, 31) - 1;

        queue<pair<int, int>> cells;
        queue<int> depths;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 0) { // Treasure
                    cells.push(make_pair(i, j));
                    depths.push(0);
                }
            }
        }

        vector<pair<int, int>> offsets = {{1, 0}, {0, -1}, {-1, 0}, {0, 1}};
        while (cells.size() > 0) {
            const auto& [r, c] = cells.front();
            int depth = depths.front();
            for (const auto& [dr, dc] : offsets) {
                if (
                    0 <= r + dr && r + dr < grid.size() 
                    && 0 <= c + dc && c + dc < grid[0].size()) {
                    int& cell = grid[r + dr][c + dc];
                    if (cell == INF) {
                        cell = depth + 1;
                        cells.push(make_pair(r + dr, c + dc));
                        depths.push(depth + 1);
                    }
                }
            }

            cells.pop();
            depths.pop();
        }
    }

    int exp(int n, int x) {
        if (x == 0) {
            return 1;
        }
        return n * exp(n, x - 1);
    }
};
