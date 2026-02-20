# Approach 1: Rotate Groups of four cells
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
        
        
# Approach 2: Reflection on row + Transpose 
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        side_len = len(matrix)

        top = 0
        bottom = side_len - 1

        while top < bottom: 
            for i in range(side_len):
                matrix[top][i], matrix[bottom][i] = matrix[bottom][i], matrix[top][i]
            top += 1
            bottom -= 1
        
        for i in range(side_len):
            for j in range(i+1, side_len):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix
        
        