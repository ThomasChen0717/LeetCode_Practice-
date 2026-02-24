# Approach 1: Evaluating Boundaries
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 1

        while i < n and nums[i-1] < nums[i]: 
            i += 1
        
        p = i - 1
        if p == 0: return False 

        while i < n and nums[i-1] > nums[i]: 
            i += 1
        q = i - 1
        if p == q or q == n - 1: return False 
        
        while i < n and nums[i - 1] < nums[i]: 
            i += 1
        
        return i == n

# Approach 2: Count Turning Points '
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[0] >= nums[1]:
            return False

        count = 1
        for i in range(2, n):
            if nums[i - 1] == nums[i]:
                return False
            if (nums[i - 2] - nums[i - 1]) * (nums[i - 1] - nums[i]) < 0:
                count += 1

        return count == 3