class Solution {
public:
    int trailingZeroes(int n) {
        int total = 0;

        for (int i = 0; i <= n; i++) {
            int j = i;
            while (j % 5 == 0 && j > 0) {
                j /= 5;
                total++;
            }
        }

        return total;
    }
};
