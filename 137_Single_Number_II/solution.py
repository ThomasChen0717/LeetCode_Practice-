# Approach 1: Bit Manipulation:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        loner = 0

        for shift in range(32): 
            bitSum = 0

            for num in nums: 
                bit = (num >> shift) & 1
                bitSum += bit
            
            loner_bit = bitSum % 3
            loner = loner | (loner_bit << shift)
        
        if loner >= (1 << 31):
            loner = loner - (1 << 32)

        return loner

# Approach 2: Generalized Bit Manipulation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0

        for num in nums: 
            seen_once = (seen_once ^ num) & (~seen_twice)
            seen_twice = (seen_twice ^ num) & (~seen_once)
        
        return seen_once