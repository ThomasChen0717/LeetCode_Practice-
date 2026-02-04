# Approach: Sorting and Two Pointers
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3: return sum(nums) 
        
        nums.sort() 

        diff = float('inf') 

        for i in range(len(nums) - 2):
            left = i + 1 
            right = len(nums) - 1

            while left < right: 
                curr_sum = nums[left] + nums[right] + nums[i]
                if abs(target - curr_sum) < abs(diff):
                    diff = target - curr_sum
                    
                if diff == 0: return target 

                if curr_sum > target: 
                    right -= 1
                else: 
                    left += 1
                
        return target - diff







