# Approach 1: Dynamic Programming
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        hold = [0] * n
        free = [0] * n
        

        hold[0] = -prices[0] 

        for i in range(1, n): 
            hold[i] = max(hold[i-1], free[i-1] - prices[i]) 
            free[i] = max(free[i-1], hold[i-1] + prices[i] - fee)

        return free[n - 1]

# Approach 2: Space Optimization
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        hold = -prices[0]
        free = 0
    
        for i in range(1, n): 
            tmp_hold = hold
            hold = max(hold, free - prices[i]) 
            free = max(free, tmp_hold + prices[i] - fee)

        return free