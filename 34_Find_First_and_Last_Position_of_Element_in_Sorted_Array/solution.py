# Approach: Binary Search on left and right bounds
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_bound = self.findBound(nums, target, True) 
        if left_bound == -1: return [-1, -1] 

        right_bound = self.findBound(nums, target, False) 

        return [left_bound, right_bound]


    def findBound(self, nums, target, isFirst): 
        lo, hi = 0, len(nums) - 1 

        while lo <= hi: 
            mid = lo + (hi - lo) // 2
            if nums[mid] == target: 
                if isFirst: 
                    if mid == lo or nums[mid - 1] < target: 
                        return mid
                    
                    hi = mid - 1
                else: 
                    if mid == hi or nums[mid + 1] > target: 
                        return mid 
                    lo = mid + 1
            elif nums[mid] > target: 
                hi = mid - 1
            else: 
                lo = mid + 1
        
        return -1