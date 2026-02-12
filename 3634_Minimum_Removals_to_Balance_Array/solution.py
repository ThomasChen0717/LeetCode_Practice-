# Approach: Sorting + Two Pointers
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort() 

        cnt = float('inf')

        right = 0

        for left in range(n): 
            while right < n and nums[right] <= nums[left] * k:
                right += 1 
            cnt = min(cnt, n - (right - left)) 

        
        return cnt
                
