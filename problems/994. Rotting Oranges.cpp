class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int fresh = 0;
        queue<pair<pair<int, int>, int>> rotten = queue<pair<pair<int, int>, int>>{};

        if (grid.size() == 0) {
            return 0;
        }

        // Find fresh and rotten
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 1) {
                    fresh++;
                } else if(grid[i][j] == 2) {
                    rotten.push(make_pair(make_pair(i, j), 0));
                }
            }
        }

        int final_elapsed = 0;
        while (rotten.size() > 0) {
            const auto& [p, elapsed] = rotten.front();
            const auto& [i, j] = p;
            final_elapsed = elapsed;
            if (i > 0) {
                if (grid[i - 1][j] == 1) {
                    grid[i - 1][j] = 2;
                    rotten.push(make_pair(make_pair(i - 1, j), elapsed + 1));
                    fresh--;
                }
            } if (i < grid.size() - 1) {
                if (grid[i + 1][j] == 1) {
                    grid[i + 1][j] = 2;
                    rotten.push(make_pair(make_pair(i + 1, j), elapsed + 1));
                    fresh--;
                }
            } if (j > 0) {
                if (grid[i][j - 1] == 1) {
                    grid[i][j - 1] = 2;
                    rotten.push(make_pair(make_pair(i, j - 1), elapsed + 1));
                    fresh--;
                }
            } if (j < grid[0].size() - 1) {
                if (grid[i][j + 1] == 1) {
                    grid[i][j + 1] = 2;
                    rotten.push(make_pair(make_pair(i, j + 1), elapsed + 1));
                    fresh--;
                }
            }
            rotten.pop();
        }
        return fresh == 0 ? final_elapsed : -1;
    }
};

