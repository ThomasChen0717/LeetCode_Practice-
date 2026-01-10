# Approach 1: Simple Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []

# Approach 2: One Pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num:Dict[int, int] = {}

        for i in range(len(nums)):
            if (target - nums[i]) in num: return [num[target - nums[i]], i]
            else: num[nums[i]] = i
        
        return []


