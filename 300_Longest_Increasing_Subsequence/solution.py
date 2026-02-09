# Approach 1: DP 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums) 

        for i in range(1, len(nums)): 
            dp[i] = max((dp[j] + 1 for j in range(i) if nums[j] < nums[i]), default=dp[i])
        
        return max(dp)

# Approach 2: Intelligent Build
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]] 
        for num in nums[1:]: 
            if num > sub[-1]:
                sub.append(num)
            else: 
                for i in range(len(sub)): 
                    if num <= sub[i]: 
                        sub[i] = num
                        break 

        return len(sub)

# Approach 3: Intelliegent Buid + Binary Search
class Solution:
    def binSearch(self, nums, target): 
        lo = 0
        hi = len(nums)

        while lo < hi: 
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target: 
                hi = mid 
            else: 
                lo = mid + 1
        
        return lo


    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]] 
        for num in nums[1:]: 
            if num > sub[-1]:
                sub.append(num)
            else: 
                idx = self.binSearch(sub, num)
                sub[idx] = num
        return len(sub)

