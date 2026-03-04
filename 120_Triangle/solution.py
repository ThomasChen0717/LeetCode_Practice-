# Approach 1: Dynamic Programming Bottom-Up In-place 
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)): 
            for j in range(i + 1):
                if j == 0: 
                    triangle[i][j] = triangle[i-1][j] + triangle[i][j] 
                elif j == len(triangle[i]) - 1: 
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i][j] 
                else: 
                    triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]

        return min(triangle[-1])

# Approach 2: Dynamic Programming Bottom-Up Reverse Triangle Auxiliary Space
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_row = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1): 
            curr_row = []
            for j in range(i + 1):
                curr_row.append(min(prev_row[j], prev_row[j+1]) + triangle[i][j]) 
            print(curr_row)
            prev_row = curr_row

        return prev_row[0]

# Approach 3:  Top Down Dynamic Programming
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = [[None] * len(row) for row in triangle]

        def min_path(row, col):
            if memo[row][col] is not None:
                return memo[row][col]

            path = triangle[row][col]

            if row < n - 1:
                path += min(min_path(row + 1, col),
                            min_path(row + 1, col + 1))

            memo[row][col] = path
            return path

        return min_path(0, 0)