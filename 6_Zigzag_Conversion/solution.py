# Approach 1: Following the Zigzag Pattern
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        n = len(s) 

        columns_per_sec = numRows - 1
        secs = ceil(n / (2 * numRows - 2)) 

        numCols = secs * columns_per_sec 

        matrix = [[""] * numCols for _ in range(numRows)]

        r, c = 0, 0 
        idx = 0

        while idx < n: 
            while r < numRows and idx < n: 
                matrix[r][c] = s[idx] 
                r += 1
                idx += 1
            
            r -= 2
            c += 1
            
            while r > 0 and c < numCols and idx < n: 
                matrix[r][c] = s[idx]
                r -= 1 
                c += 1
                idx += 1

        ans = "".join("".join(r) for r in matrix)

        return ans

# Approach 2: String Traversal
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        n = len(s) 

        answer = [] 

        chars_in_section = 2 * (numRows - 1) 

        for currRow in range(numRows): 
            index = currRow 
            while index < n: 
                answer.append(s[index]) 

                if currRow != 0 and currRow != numRows - 1: 
                    chars_in_between = chars_in_section - 2 * currRow 
                    second_index = index + chars_in_between 
                
                    if second_index < n: 
                        answer.append(s[second_index])
                
                index += chars_in_section 
        
        return ''.join(answer)