# Approach 1: Count Sort 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0] * 3
        for i in range(len(nums)): 
            freq[nums[i]] += 1

        k = 0
        for i in range(3): 
            for j in range(freq[i]): 
                nums[k] = i 
                k += 1


# Approach 2: One Pass Three Pointers
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        curr, p0, p2 = 0,0, n-1

        while curr <= p2:
            if nums[curr] == 0: 
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2: 
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else: 
                curr += 1
        


