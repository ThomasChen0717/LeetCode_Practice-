# Approach: Space Optimized Dynamic Programming
class Solution:
    def minimumDistance(self, word: str) -> int:

        def dist(a:int, b:int) -> int: 
            if a == -1 or b == -1: 
                return 0 
            
            ax, ay = a // 6, a % 6
            bx, by = b // 6, b % 6

            return abs(bx-ax) + abs(by - ay) 


        dp = {(-1, -1): 0}

        for ch in word: 
            c = ord(ch) - ord('A') 
            new_dp = {} 

            for (f1, f2), cost in dp.items(): 
                state1 = (c, f2) 
                cost1 = cost + dist(c, f1)
                if state1 not in new_dp or cost1 < new_dp[state1]: 
                    new_dp[state1] = cost1 
                
                state2 = (f1, c) 
                cost2 = cost + dist(c, f2)
                if state2 not in new_dp or cost2 < new_dp[state2]: 
                    new_dp[state2] = cost2 
            dp = new_dp 
        
        return min(dp.values())