using namespace std;

#include <vector>
#include <iostream>

int C(int n, int m) {
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int j = 0; j <= m; j++) {
        for (int i = 0; i <= n; i++) {
            if (i == j || j == 0) {
                dp[i][j] = 1;
            } else if (i != 0) {
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1];
            }
        }
    }

    return dp[n][m];
}

int main(int argc, char** argv) {
    cout << C(stoi(argv[1]), stoi(argv[2])) << endl;
    return 0;
}
