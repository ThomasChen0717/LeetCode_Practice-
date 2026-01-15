# Approach 1: Brute Force
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = set()
            for i in range(start, end + 1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True

        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res

# Approach 2: Sliding Window 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {} 

        left = right = 0

        max_len = 0

        while right < len(s):
            curr = s[right] 
            chars[curr] = chars.get(curr,0) + 1 

            while chars[curr] > 1: 
                l = s[left] 
                chars[l] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        
        return max_len
    
# Approach 3: Sliding Window Optimized
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s) 
        ans = 0
        charToNextIndex = {} 

        i = 0 
        for j in range(n): 
            if s[j] in charToNextIndex: 
                i = max(charToNextIndex[s[j]], i)
            
            ans = max(ans, j - i + 1) 
            charToNextIndex[s[j]] = j + 1

        return ans




