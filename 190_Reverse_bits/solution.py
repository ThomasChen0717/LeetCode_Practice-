# Approach 1: Bit by Bit
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31 
        while n: 
            ret += (n & 1) << power 
            n = n >> 1 
            power -= 1
        
        return ret

# Approach 2: Byte by Byte with Memoization
class Solution:
    def __init__(self):
        self.cache = {}

    def reverseBits(self, n: int) -> int:
        ret, power = 0, 24
        while n:
            byte = n & 0xFF
            if byte not in self.cache:
                self.cache[byte] = self.reverseByte(byte)
            ret += self.cache[byte] << power
            n >>= 8
            power -= 8
        return ret

    def reverseByte(self, byte):
        return (byte * 0x0202020202 & 0x010884422010) % 1023

# Approach 3: Mask and Shift
class Solution:
    def reverseBits(self, n: int) -> int:
        n = (n >> 16) | (n << 16)
        n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
        n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
        n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
        return n
