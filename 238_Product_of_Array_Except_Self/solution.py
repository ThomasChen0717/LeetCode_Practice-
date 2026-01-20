# Approach 1: Prefix Product and Suffix Product 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L, R, ans = [0] * n, [0] * n, [0] * n

        L[0] = 1
        for i in range(1, n): 
            L[i] = L[i-1] * nums[i-1]

        R[n - 1] = 1

        for i in range(n-2, -1, -1): 
            R[i] = R[i + 1] * nums[i + 1]

        for i in range(n): 
            ans[i] = L[i] * R[i] 

        return ans 

# Approach 2: Constant Space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        ans[0] = 1
        for i in range(1, n): 
            ans[i] = ans[i-1] * nums[i-1]

        R = 1
        for i in range(n-1, -1, -1): 
            ans[i] = ans[i] * R 
            R *= nums[i]  

        return ans 
