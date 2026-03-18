# Approach 1: Binary Search
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x 

        left, right = 2, x // 2

        while left < right:
            mid = right - (right - left) // 2
            power = mid * mid

            if power > x: 
                right = mid - 1
            else: 
                left = mid
        
        return right

# Approach 2: Recursion + Bit Shifts
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = self.mySqrt(x >> 2) << 1
        right = left + 1
        return left if right * right > x else right

# Approach 3: Newton's Method
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + float(x) / x0) / 2

        return int(x1)