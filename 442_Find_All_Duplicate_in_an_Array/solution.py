# Approach 1： Cyclic Sort
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

            

        i = 0
        while i < n: 
            correctIdx = nums[i] - 1

            if nums[i] != nums[correctIdx]: 
                nums[i], nums[correctIdx] = nums[correctIdx], nums[i]
            else: 
                i += 1
        
        for i in range(n): 
            if nums[i] != i + 1: 
                res.append(nums[i])

        return res

# Approach 2: In-Place Modification
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        for num in nums: 
            if nums[abs(num) - 1] < 0: 
                res.append(abs(num)) 
                continue
            nums[abs(num) - 1] *= -1

        return res
            
    
    