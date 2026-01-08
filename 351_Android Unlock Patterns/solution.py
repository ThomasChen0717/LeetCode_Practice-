#Approach 1: Naive Backtracking
class Solution:
    SINGLE_STEP_MOVES = [
            (0,1), 
            (0, -1), 
            (1, 0),
            (-1, 0), 
            (1, 1), 
            (-1, 1), 
            (1, -1),
            (-1, -1), 
            (-2, 1), 
            (2, 1),
            (-2, -1),
            (2, -1), 
            (1, -2),
            (-1, -2),
            (1, 2),
            (-1, 2),
    ] 

    SKIP_MOVES = [
        (0, 2), 
        (2, 0),
        (0, -2),
        (-2, 0), 
        (2, 2), 
        (-2, 2),
        (-2, -2),
        (2, -2)
    ]
    def numberOfPatterns(self, m: int, n: int) -> int: 
        total_patterns = 0 
        for row in range(3):
            for col in range(3):
                visited_dots = [[False for _ in range(3)] for _ in range(3)]
        
                total_patterns += self.count_patterns_from_dot(
                            m, n, 1, row, col, visited_dots
                        )
        
        return total_patterns 
    
    def count_patterns_from_dot(self, m, n, curr_len, curr_row, curr_col, visited): 
        if curr_len > n: return 0 

        valid_patterns = 0 

        if curr_len >= m: 
            valid_patterns += 1
        
        visited[curr_row][curr_col] = True 

        for move in self.SINGLE_STEP_MOVES: 
            new_r = curr_row + move[0]
            new_c = curr_col + move[1] 
            if self.is_valid_move(new_r, new_c, visited): 
                valid_patterns += self.count_patterns_from_dot(m, n, curr_len + 1, new_r, new_c, visited)
            
        for move in self.SKIP_MOVES:
            new_r = curr_row + move[0]
            new_c = curr_col + move[1]
            if self.is_valid_move(new_r, new_c, visited):
                middle_r = curr_row + move[0] // 2
                middle_c = curr_col + move[1] // 2
                if visited[middle_r][middle_c]: 
                    valid_patterns += self.count_patterns_from_dot(m, n, curr_len + 1, new_r, new_c, visited)
        
        visited[curr_row][curr_col] = False 
        return valid_patterns

    def is_valid_move(self, r, c, visited):
        return 0 <= r < 3 and 0 <= c < 3 and visited[r][c] == False

#Approach 2: Optimized Backtracking
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int: 
        total_patterns = 0 
        jump = [[0 for _ in range(10)] for _ in range(10)]

        jump[1][3] = jump[3][1] = 2
        jump[4][6] = jump[6][4] = 5
        jump[7][9] = jump[9][7] = 8
        jump[1][7] = jump[7][1] = 4
        jump[2][8] = jump[8][2] = 5
        jump[3][9] = jump[9][3] = 6
        jump[1][9] = jump[9][1] = jump[3][7] = jump[7][3] = 5



        visited_numbers = [False] * 10
        total_patterns = 0

        total_patterns += (
            self._count_patterns_from_number(1, 1, m, n, jump, visited_numbers)
            * 4
        )

        total_patterns += (
            self._count_patterns_from_number(2, 1, m, n, jump, visited_numbers)
            * 4
        )

        total_patterns += self._count_patterns_from_number(
            5, 1, m, n, jump, visited_numbers
        )

        return total_patterns
    
    def _count_patterns_from_number(
        self,
        current_number: int,
        current_length: int,
        min_length: int,
        max_length: int,
        jump: list,
        visited_numbers: list,
    ) -> int: 
        if current_length > max_length: return 0 

        valid_patterns = 0 

        if current_length >= min_length: 
            valid_patterns += 1
        
        visited_numbers[current_number] = True 

        for next_number in range(1, 10):
            jump_over_number = jump[current_number][next_number]
            if not visited_numbers[next_number] and (
            jump_over_number == 0 or visited_numbers[jump_over_number]):
                valid_patterns += self._count_patterns_from_number      (next_number,
                    current_length + 1,
                    min_length,
                    max_length,
                    jump,
                    visited_numbers,
                )
        
        visited_numbers[current_number] = False
        return valid_patterns

# Approach 3: 
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int: 
        total_patterns = 0 
        jump = [[0 for _ in range(10)] for _ in range(10)]

        jump[1][3] = jump[3][1] = 2
        jump[4][6] = jump[6][4] = 5
        jump[7][9] = jump[9][7] = 8
        jump[1][7] = jump[7][1] = 4
        jump[2][8] = jump[8][2] = 5
        jump[3][9] = jump[9][3] = 6
        jump[1][9] = jump[9][1] = jump[3][7] = jump[7][3] = 5



        visited_numbers = 0
        total_patterns = 0

        dp = [[-1] * (1 << 10) for _ in range(10)] 

        total_patterns += (
            self._count_patterns_from_number(1, 1, m, n, jump, visited_numbers, dp)
            * 4
        )

        total_patterns += (
            self._count_patterns_from_number(2, 1, m, n, jump, visited_numbers, dp)
            * 4
        )

        total_patterns += self._count_patterns_from_number(
            5, 1, m, n, jump, visited_numbers, dp
        )

        return total_patterns
    
    def _count_patterns_from_number(
        self,
        current_number: int,
        current_length: int,
        min_length: int,
        max_length: int,
        jump: list,
        visited_numbers: int,
        dp: list,
    ) -> int: 
        if current_length > max_length: return 0 

        if dp[current_number][visited_numbers] != -1: 
            return dp[current_number][visited_numbers] 

        valid_patterns = 0 

        if current_length >= min_length: 
            valid_patterns += 1
        
        visited_numbers = self._set_bit(visited_numbers, current_number) 

        for next_number in range(1, 10):
            jump_over_number = jump[current_number][next_number]
            if not self._is_set(visited_numbers, next_number) and (
            jump_over_number == 0 or self._is_set(visited_numbers, jump_over_number)):
                valid_patterns += self._count_patterns_from_number      (next_number,
                    current_length + 1,
                    min_length,
                    max_length,
                    jump,
                    visited_numbers,
                    dp
                )
        
        visited_numbers = self._clear_bit(visited_numbers, current_number)

        dp[current_number][visited_numbers] = valid_patterns 

        return valid_patterns

    def _set_bit(self, num: int, position: int) -> int:
        num |= 1 << (position - 1)
        return num

    def _clear_bit(self, num: int, position: int) -> int:
        num ^= 1 << (position - 1)
        return num

    def _is_set(self, num: int, position: int) -> bool:
        bit_at_position = (num >> (position - 1)) & 1
        return bit_at_position == 1





