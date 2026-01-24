# Approach 1: Cascading
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums: 
            new_subst = []
            for curr in output: 
                temp = curr[:] 
                temp.append(num) 
                new_subst.append(temp) 
            for subst in new_subst: 
                output.append(subst) 
        
        return output

# Approach 2: Backtracking 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []        
        def backtrack(idx, curr): 
            ans.append(curr[:]) 

            for i in range(idx, len(nums)): 
                curr.append(nums[i]) 
                backtrack(i + 1, curr) 
                curr.pop() 
        
        backtrack(0, [])

        return ans

# Approach 3: Bitmasking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [] 
        n = len(nums)

        for i in range(2 ** n, 2 ** (n + 1)): 
            bitmask = bin(i)[3:] 

            ans.append([nums[j] for j in range(n) if bitmask[j] == "1"])

        return ans
        


