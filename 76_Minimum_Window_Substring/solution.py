# Approach: Sliding Window + HashMap 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if n > m: return ""

        char_map = {}
        for c in t:
            char_map[c] = char_map.get(c, 0) + 1

        idx = 0
        count = len(char_map)
        length = float("inf")

        start, end = 0, 0
        
        while end < m:
            c = s[end] 
            if c in char_map:
                char_map[c] = char_map.get(c) - 1
                if char_map[c] == 0: 
                    count -= 1

            while count == 0:
                c_start = s[start] 
                if c_start in char_map: 
                    char_map[c_start] = char_map.get(c_start) + 1
                    if(char_map.get(c_start) > 0): 
                        count += 1

                curr_len = end - start + 1
                if curr_len < length: 
                    length = curr_len
                    idx = start

                start += 1
        
            end += 1

        return s[idx:(idx + length)] if length != float("inf") else ""