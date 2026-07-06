# Approach: Sliding Window
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        target = [0] * 26
        for ch in p:
            if 'a' <= ch <= 'z': 
                target[ord(ch) - ord('a')] += 1
        
        window = [0] * 26 

        matches = 0
        i = 0

        non_zero_count = sum(1 for x in target if x > 0)

        for j in range(len(s)):
            ch = s[j]
            idx = ord(ch) - ord('a')
            window[idx] += 1

            if window[idx] == target[idx]: 
                matches += 1
            elif window[idx] - 1 == target[idx]: 
                matches -= 1
            
            if j - i + 1 > len(p): 
                left_idx = ord(s[i]) - ord('a')
                window[left_idx] -= 1

                if window[left_idx] + 1 == target[left_idx]: 
                    matches -= 1
                elif window[left_idx] == target[left_idx]: 
                    matches += 1
                
                i += 1
            
            if matches == non_zero_count: 
                res.append(i) 
            
        
        return res


