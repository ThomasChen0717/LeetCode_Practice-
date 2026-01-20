# Approach 1: Brute Force
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        for i in range(1, len(nums), 2): 
            if nums[i] != nums[i - 1]: 
                return nums[i-1] 
        return nums[-1]


# Approach 2: Binary Search 
def singleNonDuplicate(self, nums: List[int]) -> int:
    lo = 0
    hi = len(nums) - 1   
    while lo < hi:
        mid = lo + (hi - lo) // 2
        halves_are_even = (hi - mid) % 2 == 0
        if nums[mid + 1] == nums[mid]:
            if halves_are_even:
                lo = mid + 2
            else:
                hi = mid - 1
        elif nums[mid - 1] == nums[mid]:
            if halves_are_even:
                hi = mid - 2
            else:
                lo = mid + 1
        else:
            return nums[mid]
    return nums[lo]

# Approach 3: Binary Search on Even Indexes
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi: 
            mid = lo + (hi - lo) // 2
            if mid % 2 == 1: 
                mid -= 1
            if nums[mid] != nums[mid + 1]: 
                hi = mid 
            else: 
                lo = mid + 2
        
        return nums[lo]
            
        

            
        
