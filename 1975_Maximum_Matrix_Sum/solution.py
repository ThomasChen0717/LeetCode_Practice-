class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_sum = 0 
        abs_min = float('inf') 
        negative_cnt = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])): 
                if matrix[i][j] < 0: negative_cnt += 1
                absolute_val = abs(matrix[i][j])
                abs_sum += absolute_val 
                abs_min = min(abs_min, absolute_val)
        
        if negative_cnt % 2: 
            return abs_sum - abs_min * 2
        else: 
            return abs_sum

