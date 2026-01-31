# Approach 1: Horizontal Scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def findPrefix(str1, str2):
            i = 0

            while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
                i += 1
            
            return str1[:i]

        res = strs[0]
        for i in range(1, len(strs)): 
            res = findPrefix(res, strs[i]) 
        
        return res

        
# Approach 2: Vertical Scanning 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]



