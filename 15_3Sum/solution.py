# Approach 1: Sort and Use Two Pointers 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() 
        for i in range(len(nums)): 
            if nums[i] > 0: 
                break 
            if i == 0 or nums[i-1] != nums[i]: 
                self.twoSum(nums, i, res) 
        
        return res

    

    def twoSum(self, nums: List[int], pos:int, res: List[List[int]]):
        lo = pos + 1
        hi = len(nums) - 1

        target = -nums[pos]

        while lo < hi: 
            if nums[lo] + nums[hi] < target: 
                lo += 1
            elif nums[lo] + nums[hi] > target:
                hi -= 1
            else: 
                res.append([nums[pos], nums[lo], nums[hi]]) 
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1


# Approach 2: Sorting with HashSet
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1

# Approach 3:  Hash with Triplet Sorting for Duplicate Elimination
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i + 1 :]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return [list(x) for x in res]