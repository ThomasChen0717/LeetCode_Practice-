# Approach 1: Top-Down Recursion + Memo
class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.rob_from(0, nums) 
    
    def rob_from(self, i, nums): 
        if i >= len(nums): return 0 

        if i in self.memo: return self.memo[i] 

        ans = max(self.rob_from(i + 1, nums), self.rob_from(i + 2, nums) + nums[i])

        self.memo[i] = ans

        return ans

# Approach 2: Bottom-Up Dynamic Programming
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1: 
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0] 
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)): 
            dp[i] = max(dp[i - 2] + nums[i], dp[i-1])
        
        return dp[len(nums) - 1]

# Approach 3: Optimized Dynamic Programming
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1: 
            return nums[0]

        rob_skip = 0
        rob = nums[0] 

        for i in range(1, len(nums)): 
            current = max(rob, rob_skip + nums[i])

            rob_skip = rob
            rob = current
        
        return rob


