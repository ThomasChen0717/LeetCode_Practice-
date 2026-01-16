# Approach 1: Brute Force 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start : start + length]

        return ""

# Approach 2: DP 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s) 
        dp = [[False] * n for _ in range(n)] 
        ans = [0, 0] 

        for i in range(n):
            dp[i][i] = True 
        
        for i in range(n-1): 
            if s[i] == s[i+1]: 
                dp[i][i+1] = True 
                ans = [i, i+1]
        
        for diff in range(2, n): 
            for i in range(n - diff):
                j = i + diff 
                if s[i] == s[j] and dp[i+1][j-1]: 
                    dp[i][j] = True 
                    ans = [i, j] 

        i, j = ans 
        return s[i:j + 1]

# Approach 3: Expand from Center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j): 
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            return j - i - 1


        ans = [0, 0]

        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]

            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]

        i, j = ans
        return s[i : j + 1]