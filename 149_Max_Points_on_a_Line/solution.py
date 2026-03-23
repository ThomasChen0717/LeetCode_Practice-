# Approach: Normalized Slope
class Solution:
    def gcd(self, a, b): 
        a, b = abs(a), abs(b) 

        while b != 0: 
            a, b = b, a % b 
        
        return a
    
    def findSlope(self, pt1, pt2): 
        dy = pt2[1] - pt1[1] 
        dx = pt2[0] - pt1[0]

        if dx == 0:
            return (0, 1)
    
        if dy == 0:
            return (1, 0)

        div = self.gcd(dx, dy) 

        dx //= div
        dy //= div

        if dx < 0:
            dx *= -1
            dy *= -1

        return (dx, dy)
        

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n == 1: return 1

        max_len = 2

        for i in range(n-1): 
            line_dict = collections.defaultdict(int) 

            for j in range(i + 1, n): 
                slope = self.findSlope(points[i], points[j]) 
                line_dict[slope] += 1

            max_len = max(max_len, max(line_dict.values()) + 1) 
        
        return max_len


