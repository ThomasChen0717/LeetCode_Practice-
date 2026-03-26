# Approach 1: Loop and Flip
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0 
        mask = 1

        for _ in range(32): 
            if n & mask != 0: 
                cnt += 1
            
            mask <<= 1
        
        return cnt

# Approach 2: Bit Manipulation
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0 

        while n != 0: 
            cnt += 1
            n &= (n-1)
        
        return cnt
        


# Approach 3: Divide by 2 and Check Remainder
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 1

        while n != 1: 
            if n % 2 == 1: 
                cnt += 1
            n //= 2
        
        return cnt


# Approach 4: Precompute Table
class Solution:
    table = [0] * 256
    for i in range(256):
        table[i] = table[i >> 1] + (i & 1)

    def hammingWeight(self, n: int) -> int:
        return (
            self.table[n & 0xff] +
            self.table[(n >> 8) & 0xff] +
            self.table[(n >> 16) & 0xff] +
            self.table[(n >> 24) & 0xff]
        )