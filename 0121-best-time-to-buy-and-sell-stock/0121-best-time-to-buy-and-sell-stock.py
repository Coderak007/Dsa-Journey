class Solution:
    def maxProfit(self, prices):
        mini = prices[0]
        maxProfit = 0
        n = len(prices)

        for i in range(1,n):
            cost = prices[i] - mini
            maxProfit = max(maxProfit , cost)
            mini = min(mini,prices[i])

        return maxProfit            