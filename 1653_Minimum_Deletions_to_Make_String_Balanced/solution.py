# Approach 1: Three Pass
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        count_a = [0] * n
        count_b = [0] * n

        count_b[0] = 1 if s[0] == 'b' else 0
        for i in range(1, n): 
            if s[i] == 'b': 
                count_b[i] = count_b[i-1] + 1
            else: 
                count_b[i] = count_b[i-1]

        count_a[n-1] = 1 if s[n-1] == 'a' else 0
        for i in range(n-2, -1, -1): 
            if s[i] == 'a': 
                count_a[i] = count_a[i+1] + 1
            else: 
                count_a[i] = count_a[i+1]

        min_del = n

        for i in range(n): 
            min_del = min(min_del, count_a[i] + count_b[i] - 1)
        
        return min_del

# Approach 2:Two Pass two variables
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        count_a = 0
        count_b = 0

        for ch in s: 
            if ch == 'a': 
                count_a += 1

        min_del = n

        for i in range(n): 
            if s[i] == 'a': count_a -= 1

            min_del = min(min_del, count_a + count_b)

            if s[i] == 'b': count_b += 1
        
        return min_del

# Approach 3: Stack
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        stack = []

        num_del = 0 

        for ch in s: 
            if stack and stack[-1] == 'b' and ch == 'a': 
                stack.pop() 
                num_del += 1
                continue 

            stack.append(ch)
        
        return num_del

# Approach 4: DP
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        b_count = 0

        for i in range(n):
            if s[i] == "b":
                dp[i + 1] = dp[i]
                b_count += 1
            else:
                dp[i + 1] = min(dp[i] + 1, b_count)

        return dp[n]


## Approach 5: Space Optimized DP
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        min_deletions = 0
        b_count = 0

        for i in range(n):
            if s[i] == "b":
                b_count += 1
            else:
                min_deletions = min(min_deletions + 1, b_count)

        return min_deletions