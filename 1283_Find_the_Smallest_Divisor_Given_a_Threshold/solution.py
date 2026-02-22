# Approach: Binary Search
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def get_sum(divisor): 
            sm = 0 
            for num in nums: 
                if num % divisor != 0: 
                    sm += (num // divisor) + 1
                else: 
                    sm += (num // divisor)
            
            return sm 

        lo = 1
        hi = max(nums) 

        while lo < hi: 
            mid = lo + (hi - lo) // 2

            if get_sum(mid) <= threshold: 
                hi = mid
            else: 
                lo = mid + 1
        
        return lo


