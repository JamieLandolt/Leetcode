class Solution {
public:
    int countCommas(int n) {
        int total = 0;
        while (n / 1000 > 0) {
            total += (n - 999);
            n /= 1000;
        }
        return total;
    }
};
