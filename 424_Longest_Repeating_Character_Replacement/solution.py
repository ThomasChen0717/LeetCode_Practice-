# Approach 1: Sliding Window + Binary Search
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lo, hi = 1, len(s)

        while lo < hi: 
            mid = hi - (hi - lo) // 2

            if self.can_make_valid_substring(s, k, mid): 
                lo = mid
            else: 
                hi = mid - 1
        
        return lo

    
    def can_make_valid_substring(self, s:str, k:int, length:int): 
        start = 0 
        freq = {} 
        max_freq = 0
        for end in range(len(s)): 
            freq[s[end]] = freq.get(s[end], 0) + 1

            if end - start + 1> length: 
                freq[s[start]] -= 1
                start += 1
            
            max_freq = max(max_freq, freq[s[end]]) 
            if length - max_freq <= k: 
                return True 
        
        return False

# Approach 2: Sliding Window Slow
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        st = set(s) 
        max_len = 0 

        for letter in st: 
            start = 0
            count = 0
            for end in range(len(s)): 
                if s[end] == letter: 
                    count += 1
                
                while end - start - count + 1 > k: 
                    if s[start] == letter: count -= 1
                    start += 1
                
                max_len = max(max_len, end-start + 1) 

        return max_len

# Approach 3: Sliding Window Fast
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        max_freq = 0
        freq = {} 
        longest_len = 0

        for end in range(len(s)): 
            freq[s[end]] = freq.get(s[end], 0) + 1

            max_freq = max(max_freq, freq[s[end]]) 

            if end - start + 1 - max_freq > k: 
                freq[s[start]] -= 1
                start += 1
            
            longest_len = end - start + 1 

        return longest_len
