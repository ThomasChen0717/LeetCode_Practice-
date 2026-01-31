# Approach 1: Brute Force
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                min_height = inf
                for k in range(i, j + 1):
                    min_height = min(min_height, heights[k])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area

# Approach 2: Better Brute Force 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            min_height = inf
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area

# Approach 3: Divide and Conquer
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def calculateArea(heights: List[int], start: int, end: int) -> int:
            if start > end:
                return 0
            min_index = start
            for i in range(start, end + 1):
                if heights[min_index] > heights[i]:
                    min_index = i
            return max(
                heights[min_index] * (end - start + 1),
                calculateArea(heights, start, min_index - 1),
                calculateArea(heights, min_index + 1, end),
            )

        return calculateArea(heights, 0, len(heights) - 1)

# Approach 4: Divide and Conquer Optimized with Segment Tree
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0

        # Segment tree storing the index of the minimum height in each segment
        size = 1
        while size < n:
            size *= 2
        seg = [-1] * (2 * size)

        def better(i: int, j: int) -> int:
            """Return index with smaller height; handle -1 as empty."""
            if i == -1: return j
            if j == -1: return i
            if heights[i] < heights[j]: return i
            if heights[j] < heights[i]: return j
            return i  # tie-break (either is fine)

        # Build leaves
        for i in range(n):
            seg[size + i] = i
        for i in range(size + n, 2 * size):
            seg[i] = -1

        # Build internal nodes
        for i in range(size - 1, 0, -1):
            seg[i] = better(seg[2 * i], seg[2 * i + 1])

        def range_argmin(l: int, r: int) -> int:
            """Return index of minimum height in [l, r]."""
            l += size
            r += size
            res = -1
            while l <= r:
                if (l % 2) == 1:
                    res = better(res, seg[l])
                    l += 1
                if (r % 2) == 0:
                    res = better(res, seg[r])
                    r -= 1
                l //= 2
                r //= 2
            return res

        def solve(l: int, r: int) -> int:
            if l > r:
                return 0
            m = range_argmin(l, r)   # O(log n)
            best_with_min = heights[m] * (r - l + 1)
            best_left = solve(l, m - 1)
            best_right = solve(m + 1, r)
            return max(best_with_min, best_left, best_right)

        return solve(0, n - 1)

# Approach 5: Stack 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxarea = 0

        for i in range(len(heights)): 
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]: 
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1

                maxarea = max(maxarea, current_height * current_width) 
            
            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            maxarea = max(maxarea, current_height * current_width)

        return maxarea


