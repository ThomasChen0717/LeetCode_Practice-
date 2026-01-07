class Solution:
    def compress(self, chars: List[str]) -> int:
        res = 0

        i = 0

        while i < len(chars):
            cnt = 1
            while i + 1 < len(chars) and chars[i + 1] == chars[i]:
                cnt += 1
                i += 1
            
            chars[res] = chars[i]
            res += 1
            if cnt > 1: 
                power = 1
                while power * 10 <= cnt:
                    power *= 10
                
                while power > 0: 
                    chars[res] = str(cnt // power)
                    cnt %= power 
                    power //= 10 
                    res += 1
            
            i += 1
        return res 
