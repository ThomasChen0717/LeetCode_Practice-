# Approach 1: DFS 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # dirs = [up, right, down, left]
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        rows, cols = len(matrix), len(matrix[0])
        
        def dfs(r, c, direction):
            seen.add((r,c))
            traverse.append(matrix[r][c]) # preorder traversal
            for i in range(4):
                new_direction = (direction + i) % 4
                nr = r + dirs[new_direction][0]
                nc = c + dirs[new_direction][1]
                if nr < 0 or nc < 0  or nr >= rows or nc >= cols or (nr, nc) in seen:
                    continue    
                dfs(nr, nc, new_direction)
                
        seen = set()
        traverse = []
        dfs(0, 0, 1)
        return traverse

# Approach 2: Set Up Boundaries
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = [] 

        m, n = len(matrix), len(matrix[0]) 

        up = left = 0 

        down = m - 1 
        right = n - 1

        while len(res) < m * n:
            for col in range(left, right + 1): 
                res.append(matrix[up][col]) 

            for row in range(up + 1, down + 1): 
                res.append(matrix[row][right])
            
            if up != down:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[down][col])

            if left != right:
                for row in range(down - 1, up, -1):
                    res.append(matrix[row][left])
            
            left += 1
            right -= 1
            up += 1
            down -= 1
        
        return res

# Approach 3: Mark Visited
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 101
        rows, columns = len(matrix), len(matrix[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
        current_direction = 0
        change_direction = 0
        
        result = [matrix[0][0]]
        matrix[0][0] = VISITED

        while change_direction < 2:

            while True:
                
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    break
                if matrix[next_row][next_col] == VISITED:
                    break

                change_direction = 0
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = VISITED
           
            current_direction = (current_direction + 1) % 4
            change_direction += 1

        return result