# Approach 1: Use two flags 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        flag_col0 = False 
        flag_row0 = False
        
        for i in range(m): 
            if matrix[i][0] == 0: 
                flag_col0 = True 
        
        for j in range(n): 
            if matrix[0][j] == 0: 
                flag_row0 = True 
        
        for i in range(1, m):
            for j in range(1, n): 
                if matrix[i][j] == 0: 
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n): 
                if matrix[i][0] == 0 or matrix[0][j] == 0: 
                    matrix[i][j] = 0 
        
        if flag_col0: 
            for i in range(m): 
                matrix[i][0] = 0
        
        if flag_row0: 
            for j in range(n): 
                matrix[0][j] = 0


# Approach 2: Only one flag
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0