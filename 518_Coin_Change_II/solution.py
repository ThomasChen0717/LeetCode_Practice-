#Approach 1: Top-Down Dynamic Programming
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:     
        n = len(coins)
        memo = [[-1] * (amount + 1) for _ in range(n)]

        def number_of_ways(idx: int, amount:int) -> int: 
            if amount == 0: return 1 
            if idx == n: return 0 

            if memo[idx][amount] != -1: 
                return memo[idx][amount] 
            
            if coins[idx] > amount: 
                memo[idx][amount] = number_of_ways(idx +1, amount) 
            else: 
                memo[idx][amount] = number_of_ways(idx, amount - coins[idx]) + number_of_ways(idx+1, amount)
            return memo[idx][amount]


        return number_of_ways(0, amount)

#Approach 2: Bottom-Up Dynamic Programming
class Solution:
    def change(self, amount: int, coins: List[int]) -> int: 
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]

        for i in range(n): 
            dp[i][0] = 1
        
        for j in range(1, amount + 1):
            if j - coins[0] >= 0: 
                dp[0][j] += dp[0][j-coins[0]]
    
        for i in range(1, n):
            for j in range(1, amount + 1): 
                dp[i][j] = dp[i-1][j] 
                if j - coins[i] >= 0: 
                    dp[i][j] += dp[i][j - coins[i]]
        
        return dp[n-1][amount]

#Approach 3: Dynamic Programming with Space Optimization
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1) 

        dp[0] = 1

        for coin in coins: 
            for i in range(coin, amount + 1): 
                    dp[i] += dp[i - coin]

        return dp[amount] 
