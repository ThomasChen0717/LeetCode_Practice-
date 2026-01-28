# Approach 1: Brute Force
class Solution:

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(row,col): 
            seen = [False] * 10
            for i in range(3):
                for j in range(3):
                    num = grid[row + i][col + j]
                    if num < 1 or num > 9:
                        return False
                    if seen[num]:
                        return False
                    seen[num] = True

            # Check if diagonal sums are the same
            diagonal1 = (
                grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
            )
            diagonal2 = (
                grid[row + 2][col] + grid[row + 1][col + 1] + grid[row][col + 2]
            )

            if diagonal1 != diagonal2:
                return False

            # Check if all row sums are the same as the diagonal sums
            row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
            row2 = (
                grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
            )
            row3 = (
                grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
            )

            if not (row1 == diagonal1 and row2 == diagonal1 and row3 == diagonal1):
                return False

            # Check if all column sums are the same as the diagonal sums
            col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
            col2 = (
                grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
            )
            col3 = (
                grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]
            )

            if not (col1 == diagonal1 and col2 == diagonal1 and col3 == diagonal1):
                return False

            return True


        n = len(grid)
        m = len(grid[0]) 

        if m < 3 or n < 3: 
            return 0 
        
        cnt = 0 

        for i in range(n - 2): 
            for j in range(m - 2): 
                if isMagicSquare(i, j): cnt += 1
        
        return cnt



# Approach 2: Math Optimized Brute Force
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m - 2):
            for col in range(n - 2):
                if self._isMagicSquare(grid, row, col):
                    ans += 1
        return ans

    def _isMagicSquare(self, grid, row, col):
        # The sequences are each repeated twice to account for
        # the different possible starting points of the sequence
        # in the magic square
        sequence = "2943816729438167"
        sequenceReversed = "7618349276183492"

        border = []
        # Flattened indices for bordering elements of 3x3 grid
        borderIndices = [0, 1, 2, 5, 8, 7, 6, 3]
        for i in borderIndices:
            num = grid[row + i // 3][col + (i % 3)]
            border.append(str(num))

        borderConverted = "".join(border)

        # Make sure the sequence starts at one of the corners
        return (
            grid[row][col] % 2 == 0
            and (
                sequence.find(borderConverted) != -1
                or sequenceReversed.find(borderConverted) != -1
            )
            and grid[row + 1][col + 1] == 5
        )