# Approach: Digit Manipulation
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        sm = 0
        idx = 0

        while n > 0: 
            digit = n % 10
            n //= 10 

            if digit != 0: 
                x = digit * (10 ** idx) + x 
                idx += 1
                sm += digit 
        
        return x * sm