# Approach 1: Recursion 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistanceRecur(word1, word2, len(word1), len(word2))

    def minDistanceRecur(self, word1, word2, word1Index, word2Index): 
        if word1Index == 0: return word2Index 
        if word2Index == 0: return word1Index 

        if word1[word1Index - 1] == word2[word2Index - 1]: 
            return self.minDistanceRecur(word1, word2, word1Index - 1, word2Index - 1)
        else: 
            insertOperation = self.minDistanceRecur(
                word1, word2, word1Index, word2Index - 1
            )
            deleteOperation = self.minDistanceRecur(
                word1, word2, word1Index - 1, word2Index
            )
            replaceOperation = self.minDistanceRecur(
                word1, word2, word1Index - 1, word2Index - 1
            )

            return min(insertOperation, deleteOperation, replaceOperation) + 1

# Approach 2: Top Down Dynamic Programming
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [
            [None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)
        ]

        def minDistanceRecur(word1, word2, word1Index, word2Index): 
            if word1Index == 0: return word2Index 
            if word2Index == 0: return word1Index 

            if memo[word1Index][word2Index]: return memo[word1Index][word2Index]

            if word1[word1Index - 1] == word2[word2Index - 1]: 
                memo[word1Index][word2Index] = minDistanceRecur(
                    word1, word2, word1Index - 1, word2Index - 1
                )
            else: 
                insertOperation = minDistanceRecur(
                    word1, word2, word1Index, word2Index - 1
                )
                deleteOperation = minDistanceRecur(
                    word1, word2, word1Index - 1, word2Index
                )
                replaceOperation = minDistanceRecur(
                    word1, word2, word1Index - 1, word2Index - 1
                )
                memo[word1Index][word2Index] = min(insertOperation, deleteOperation, replaceOperation) + 1

            return memo[word1Index][word2Index]

        return minDistanceRecur(word1, word2, len(word1), len(word2))

# Approach 3: Bottom Up Dynamic Programming 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        if m == 0:
            return n
        if n == 0:
            return m
        
        for i in range(1, m + 1): 
            dp[i][0] = i 
        
        for j in range(1, n + 1): 
            dp[0][j] = j
        
        for i in range(1, m + 1): 
            for j in range(1, n + 1): 
                if word1[i-1] == word2[j-1]: 
                    dp[i][j] = dp[i-1][j-1] 
                else: 
                    dp[i][j] = min(dp[i-1][j],  
                                   dp[i][j-1],
                                   dp[i-1][j-1]) + 1
        
        return dp[m][n]

