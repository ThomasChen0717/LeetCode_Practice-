# Approach 1: Top Down Dynamic Programming
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1] * len(text2) for _ in range(len(text1))] 

        def get_lcs(idx1, idx2):
            if idx1 >= len(text1) or idx2 >= len(text2): return 0 

            if memo[idx1][idx2] != -1: return memo[idx1][idx2] 

            skip = get_lcs(idx1 + 1, idx2) 

            include = 0
            pos = text2.find(text1[idx1], idx2)
            if pos != -1:
                include = 1 + get_lcs(idx1 + 1, pos + 1)
            
            memo[idx1][idx2] = max(skip, include)

            return memo[idx1][idx2]
        
        return get_lcs(0, 0)

# Approach 2: Improved Top Down Dynamic Programming
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1] * len(text2) for _ in range(len(text1))] 

        def get_lcs(idx1, idx2):
            if idx1 >= len(text1) or idx2 >= len(text2): return 0 

            if memo[idx1][idx2] != -1: return memo[idx1][idx2] 

            if text1[idx1] == text2[idx2]: 
                memo[idx1][idx2] = 1 + get_lcs(idx1 + 1, idx2 + 1) 
            else: 
                memo[idx1][idx2] = max(get_lcs(idx1 + 1, idx2), get_lcs(idx1, idx2 + 1))

            return memo[idx1][idx2]
        
        return get_lcs(0, 0)

# Approach 3: Bottom Up Dynamic Programming
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for row in range(len(text1)):
            for col in range(len(text2)): 
                if text1[row] == text2[col]: 
                    dp[row + 1][col + 1] = 1 + dp[row][col] 
                else: 
                    dp[row + 1][col + 1] = max(dp[row + 1][col], dp[row][col + 1]) 
        
        return dp[len(text1)][len(text2)]

# Approach 4: Space Optimized Bottom Up Dynamic Programming
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Ensure text2 is the shorter string (optional optimization)
        if len(text2) > len(text1):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for i in range(len(text1)):
            prev = 0  # represents dp[i][j]
            for j in range(len(text2)):
                temp = dp[j + 1]  # save old dp[i][j+1]
                if text1[i] == text2[j]:
                    dp[j + 1] = 1 + prev
                else:
                    dp[j + 1] = max(dp[j + 1], dp[j])
                prev = temp

        return dp[-1]


