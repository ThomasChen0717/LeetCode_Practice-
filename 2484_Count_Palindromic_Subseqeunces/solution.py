# Approach 1: Backtracking
class Solution:
    self.cnt = 0

    def checkPalindrome(self, subseq):
        left = 0
        right = len(subseq) - 1

        while left < right: 
            if subseq[left] != subseq[right]: return False 
            left += 1
            right -= 1
        
        return True


    def backtrack(self, s, idx, curr): 
        if len(curr) == 5: 
            if self.checkPalindrome(curr): 
                self.cnt += 1
            return 
        
        if idx == len(s): 
            return 
        
        for i in range(idx, len(s)):
            curr.append(s[i])
            self.backtrack(s, i+1, curr)
            curr.pop() 


    def countPalindromes(self, s: str) -> int:
        self.backtrack(s, 0, []) 

        return self.cnt

# Approach 2: Dynamic Programming
class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        if n < 5:
            return 0

        suffix = [[[0] * 10 for _ in range(10)] for _ in range(n)]

        singles = [0] * 10

        singles[int(s[n-1])] += 1

        for i in range(n - 2, -1, -1):
            curr_num = int(s[i])

            for a in range(10):
                for b in range(10):
                    suffix[i][a][b] = suffix[i + 1][a][b]

            for x in range(10):
                suffix[i][curr_num][x] += singles[x]

            singles[curr_num] += 1
        
        res = 0

        singles = [0] * 10

        singles[int(s[0])] += 1

        prefix = [[0] * 10 for _ in range(10)]

        for i in range(1, n-1): 
            curr_num = int(s[i])
            
            if i >= 2 and i <= n - 3:
                for a in range(10):
                    for b in range(10):
                        res = (res + prefix[a][b] * suffix[i + 1][b][a]) % MOD 
            
            for x in range(10): 
                prefix[x][curr_num] += singles[x] 
            
            singles[curr_num] += 1
            
        
        return res

        

            


        