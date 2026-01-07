# Approach 1: Sorting
class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)
        
# Approach 2: Two Pointers
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        res = [0] * n

        for i in range(n-1, -1, -1): 
            num_left = nums[left]
            num_right = nums[right]
            if num_left * num_left < num_right * num_right: 
                res[i] = num_right * num_right
                right -= 1
            else: 
                res[i] = num_left * num_left
                left += 1
            
        return res