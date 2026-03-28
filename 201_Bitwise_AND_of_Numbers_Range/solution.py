# Approach 1: Bit Shift
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right: 
            left >>= 1
            right >>= 1
            shift += 1
        
        return left << shift

# Approach 2: Brian Kernighan's Algorithm
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right = right & (right - 1)
        return right