# Approach 1: Brute Force 
class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            s = str(i)
            if "3" in s or "4" in s or "7" in s:
                continue
            if "2" in s or "5" in s or "6" in s or "9" in s:
                count += 1
        return count



# Approach 2: Dynamic Programming
class Solution:
    def rotatedDigits(self, n: int) -> int:
        memo = {}
        BAD = {"3", "4", "7"}
        GOOD = {"2", "5", "6", "9"}
        digits = str(n)

        def dp(pos, tight, changed, started): 
            if pos == len(digits): 
                return 1 if changed and started else 0 

            key = (pos, tight, changed, started)
            if key in memo:
                return memo[key]
            
            limit = int(digits[pos]) if tight else 9
            ans = 0
            
            for d in range(limit + 1):
                digit = str(d) 

                new_tight = tight and d == limit

                if not started and d == 0:
                    ans += dp(pos + 1, new_tight, changed, False)
                    continue
                
                if digit in BAD: 
                    continue
                
                new_changed = changed or (digit in GOOD)
                ans += dp(pos + 1, new_tight, new_changed, True)
            
            memo[key] = ans
            return ans

        return dp(0, True, False, False)