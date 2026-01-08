class Solution:
    def isVowel(self, c) -> bool: 
        return c in "aeiouAEIOU"

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0 
        right = len(s) - 1

        while left < right: 
            while left < len(s) and not self.isVowel(s[left]): 
                left += 1
            
            while right >= 0 and not self.isVowel(s[right]): 
                right -= 1 

            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1 
        
        return "".join(s)
