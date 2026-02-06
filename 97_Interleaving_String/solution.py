# Approach 1: Brute Force Recursion
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False


        def isInterleave_rec(p1, p2, p3): 
            if p3 == len(s3): return True 
            
            ok = False
            if p1 < len(s1) and s1[p1] == s3[p3]: 
                ok |= isInterleave_rec(p1 + 1, p2, p3 + 1)
            
            if p2 < len(s2) and s2[p2] == s3[p3]: 
                ok |= isInterleave_rec(p1, p2 + 1, p3 + 1) 
            
            return ok
        
        return isInterleave_rec(0, 0, 0)

# Approach 2: Recursion with Memoization
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = [[-1] * len(s2) for _ in range(len(s1))]

        def isInterleave_rec(p1, p2, p3): 
            if p1 == len(s1): return s2[p2:] == s3[p3:]
            if p2 == len(s2): return s1[p1:] == s3[p3:]

            if memo[p1][p2] != -1: 
                return memo[p1][p2] == 1
            
            ok = False
            if s1[p1] == s3[p3]: 
                ok |= isInterleave_rec(p1 + 1, p2, p3 + 1)
            
            if s2[p2] == s3[p3]: 
                ok |= isInterleave_rec(p1, p2 + 1, p3 + 1) 
            
            memo[p1][p2] = 1 if ok else 0
            
            return ok
        
        return isInterleave_rec(0, 0, 0)

# Approach 3: 2D Dynamic Programming
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
 

        for i in range(len(s1) + 1): 
            for j in range(len(s2) + 1): 
                if i == 0 and j == 0: dp[i][j] = True 
                elif i == 0: 
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[j - 1]
                elif j == 0: 
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i - 1]
                else: 
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[len(s1)][len(s2)]

# Approach 4: Using 1D Dynamic Programming
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [False] * (len(s2) + 1)
 

        for i in range(len(s1) + 1): 
            for j in range(len(s2) + 1): 
                if i == 0 and j == 0: dp[j] = True 
                elif i == 0: 
                    dp[j] = dp[j-1] and s2[j-1] == s3[j - 1]
                elif j == 0: 
                    dp[j] = dp[j] and s1[i-1] == s3[i - 1]
                else: 
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[len(s2)]

