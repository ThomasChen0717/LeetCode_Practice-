# Approach 1: 2D Dynamic Programming
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices) 

        if n <= 1: return 0 

        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]

        for j in range(k + 1):
            dp[0][j][0] = 0

        dp[0][0][1] = float('-inf')

        for j in range(1, k + 1):
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            dp[i][0][0] = 0
            dp[i][0][1] = float('-inf')

            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        return dp[n-1][k][0] 

# Approach 2: 1D Dynamic Programming 
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices) 

        if n <= 1: return 0 

        if k == 0: return 0 

        profit = [0] * (k+1)
        cost = [float('inf')] * (k+1)

        for price in prices: 
            for i in range(1, k+1): 
                cost[i] = min(cost[i], price - profit[i-1])
                profit[i] = max(profit[i], price - cost[i])
        return profit[k]
