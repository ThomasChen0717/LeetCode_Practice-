# Approach 1: Hashset 
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = set()

        for i in range(k, len(s)+1):
            tmp = s[i-k:i]
            if tmp not in got:
                got.add(tmp)
                need -= 1
                # return True when found all occurrences
                if need == 0:
                    return True
        return False

# Approach 2: Hashset with custom hash function
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = [False] * need 
        all_one = need - 1
        hash_val = 0 

        for i in range(len(s)):
            hash_val = ((hash_val << 1) & all_one) | int(s[i]) 

            if i >= k - 1 and got[hash_val] is False: 
                got[hash_val] = True 
                need -= 1
                if need == 0: 
                    return True 
                
        return False
