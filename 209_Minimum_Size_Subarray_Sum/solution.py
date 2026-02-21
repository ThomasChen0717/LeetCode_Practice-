# Approach: Sliding Window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float('inf') 

        left = 0

        curr_sm = 0
        
        for end in range(len(nums)): 
            curr_sm += nums[end]

            while curr_sm >= target: 
                minimum = min(minimum, end - left + 1) 
                curr_sm -= nums[left]
                left += 1
            
        return minimum if minimum != float('inf') else 0