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