# Approach 1: Sorting
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    str1 = list(s)
    str2 = list(t)

    str1.sort()
    str2.sort()

    return str1 == str2


# Approach 2: Frequency Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = [0] * 26

        for i in range(len(s)):
            sDict[ord(s[i]) - ord('a')] += 1
            sDict[ord(t[i]) - ord('a')] -= 1
        
        return all(count == 0 for count in sDict)