# Approach 1: Counting Factors of 5
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0

        for i in range(5, n+1, 5): 
            current = i
            while current % 5 == 0: 
                zero_count += 1
                current //= 5
        
        return zero_count

# Approach 2: Counting Factors of 5 (Optimal)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0

        power_of_five = 5

        while n >= power_of_five: 
            zero_count += n // power_of_five 
            power_of_five *= 5
        
        return zero_count