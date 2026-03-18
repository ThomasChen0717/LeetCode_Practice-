# Approach 1: Binary Exponentiation Recursive
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0 
        if n < 0: return 1.0 / self.myPow(x, -n)

        if n % 2 == 1: 
            return x * self.myPow(x * x, (n-1) / 2)
        else:
            return self.myPow(x*x, n / 2)

# Approach 2: Binary Exponentiation Iterative
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1 

        if n < 0: 
            n = -n 
            x = 1.0 / x

        result = 1
        while n != 0: 
            if n % 2 == 1: 
                result *= x 
                n -= 1
            
            x *= x
            n //= 2
        
        return result
