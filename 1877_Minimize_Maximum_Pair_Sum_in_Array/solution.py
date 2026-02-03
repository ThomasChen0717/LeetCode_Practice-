# Approach: Sort the array then pair the smallest with the Largest 
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        maxSum = 0

        for i in range(len(nums) // 2): 
            maxSum = max(maxSum, nums[i] + nums[len(nums) - i - 1])
        
        return maxSum