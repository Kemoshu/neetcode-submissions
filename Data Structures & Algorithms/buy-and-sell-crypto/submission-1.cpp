class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxim = 0, low = prices[0];
        for (int i = 1; i < prices.size(); i++) {
            low = min(low, prices[i]);
            maxim = max(maxim, prices[i] - low);
        }
        return maxim;
    }
};
