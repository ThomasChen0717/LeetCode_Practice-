class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = len(strs[0]) 
        n = len(strs) 
        cnt = 0

        for i in range(cols): 
            for j in range(1, n): 
                if strs[j][i] < strs[j-1][i]: 
                    cnt += 1
                    break
        
        return cnt
