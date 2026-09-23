int binaryKnapsack(vector<int> values, vector<int> weights) {
    // values = [1, 4, 6, 2, 3]
    // weights = [3, 2, 2, 1, 4]
    // W = 10
    //
    // dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i]] + values[i])

    vector<int> dp(values.size() + 1, 0);

    for (int i = 0; i < value.size() + 1; i++) {
        for (int w = 0; w < W; w++) {
        }
        if (i == 0) {
            dp[i][0] = 0;
        }

    }

}
