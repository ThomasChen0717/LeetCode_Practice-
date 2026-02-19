# Approach 1: Brute Force Sorting 
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def poly(x): 
            return (a * x * x) + (b * x) + c 
        
        for i in range(len(nums)): 
            nums[i] = poly(nums[i]) 
        
        nums.sort()

        return nums

# Approach 2: Two Pointers 4
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def poly(x): 
            return (a * x * x) + (b * x) + c 
        
        left, right = 0, len(nums) - 1
        res = []

        if a < 0: 
            while left <= right: 
                poly_l = poly(nums[left]) 
                poly_r = poly(nums[right]) 

                if poly_l < poly_r: 
                    res.append(poly_l)
                    left += 1
                else: 
                    res.append(poly_r)
                    right -= 1
        else: 
            while left <= right: 
                poly_l = poly(nums[left]) 
                poly_r = poly(nums[right]) 

                if poly_l > poly_r: 
                    res.append(poly_l)
                    left += 1
                else: 
                    res.append(poly_r)
                    right -= 1
            res.reverse()
        
        return res


        