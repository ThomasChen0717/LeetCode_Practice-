class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i + 1]: 
            i -= 1
        
        if i >= 0: 
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            self.swap(i, j, nums)
        
        self.reverse(i + 1, nums)

    def swap(self, i: int, j:int, nums:List[int]): 
        temp = nums[i] 
        nums[i] = nums[j]
        nums[j] = temp

    def reverse(self, idx:int, nums:List[int]): 
        i, j = idx, len(nums) - 1
        while i < j: 
            self.swap(i, j, nums) 
            i += 1
            j -= 1