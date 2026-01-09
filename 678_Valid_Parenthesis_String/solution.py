# Approach 1: Top-Down Dynamic Programming
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s) 
        memo = [[-1] * n for _ in range(n)] 
        return self.is_valid_string(0, 0, s, memo)
    
    def is_valid_string(self, index, open_count, s, memo) -> bool: 
        if index == len(s): return open_count == 0 

        if memo[index][open_count] != -1: 
            return memo[index][open_count] == 1 
        
        is_valid = False
        if s[index] == '*': 
            is_valid |= self.is_valid_string(index + 1, open_count + 1, s, memo)
            if open_count > 0: 
                is_valid |= self.is_valid_string(index + 1, open_count - 1, s, memo)
            is_valid |= self.is_valid_string(index + 1, open_count, s, memo)
        elif s[index] == '(': 
            is_valid |=  self.is_valid_string(index + 1, open_count + 1, s, memo) 
        elif open_count > 0: 
            is_valid |=  self.is_valid_string(index + 1, open_count - 1, s, memo) 
        memo[index][open_count] = 1 if is_valid else 0 
        
        return is_valid

# Approach 2: Bottom-Up Dynamic Programming
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s) 

        dp = [[False] * (n+1) for _ in range(n+1)]

        dp[0][0] = True

        for i in range(n):
            for j in range(i + 1): 
                if s[i] == '*': 
                    dp[i + 1][j + 1] |= dp[i][j] 
                    dp[i + 1][j] |= dp[i][j]
                    if j > 0: 
                        dp[i + 1][j - 1] |= dp[i][j] 
                elif s[i] == '(': 
                    dp[i+1][j+1] |= dp[i][j]
                elif j > 0: 
                    dp[i + 1][j - 1] |= dp[i][j] 
                

        return dp[n][0]

# Approach 3: Two Stacks 
class Solution:
    def checkValidString(self, s: str) -> bool:
        openBracks = []
        asterisks = [] 


        for i in range(len(s)):
            if s[i] == '(': openBracks.append(i)
            elif s[i] == '*': asterisks.append(i)
            else: 
                if openBracks: openBracks.pop()
                elif asterisks: asterisks.pop() 
                else: return False 
        
        while openBracks and asterisks: 
            if openBracks[-1] > asterisks[-1]: return False 
            else: 
                openBracks.pop()
                asterisks.pop() 

        if openBracks: return False 
        
        return True

## Approach 4: Two Pointers
class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount = 0
        closeCount = 0

        right = len(s) - 1

        for left in range(len(s)): 
            if s[left] == '(' or s[left] == '*': 
                openCount += 1
            else: 
                openCount -= 1
            
            if s[right] == ')' or s[right] == '*': 
                closeCount += 1
            else: 
                closeCount -= 1
            
            if openCount < 0 or closeCount < 0: 
                return False 
            
            right -= 1

        return True
