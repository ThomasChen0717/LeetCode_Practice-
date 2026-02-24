# Approach 1: Recursion with Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n 

        def climb(curr): 
            if curr > n: 
                return 0 
            if curr == n: 
                return 1 
            
            if memo[curr] != -1: return memo[curr] 

            one_step = climb(curr + 1) 
            second_step = climb(curr + 2)

            memo[curr] = one_step + second_step

            return memo[curr]
        
        return climb(0) 

# Approach 2: Dynamic Programming
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]

# Approach 3: Fibonacci Number
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        first = 1
        second = 2

        for i in range(2, n):
            third = first + second
            first = second
            second = third

        return second
