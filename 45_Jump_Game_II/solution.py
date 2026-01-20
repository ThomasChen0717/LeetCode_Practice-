# Approach 1: Greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, n = 0, len(nums) 
        cur_end, cur_far = 0, 0 

        for i in range(n-1): 
            if cur_end == n-1: return ans
            
            cur_far = max(cur_far, i + nums[i]) 

            if i == cur_end:
                ans += 1
                cur_end = cur_far
        
        return ans

# Approach 2: Dynamic Programming
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]
