# Approach 1: Brute Force 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0 
        n = len(height)

        for i in range(n):
            for j in range(i+1, n):
                dist = j - i 
                container_ht = min(height[i], height[j])
                max_area = max(max_area, dist * container_ht) 
        
        return max_area


# Approach 2: Two Pointers
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0 

        while left < right: 
            dist = right - left
            if height[left] < height[right]: 
                container_ht = height[left]
                left += 1 
            else: 
                container_ht = height[right]
                right -= 1
        
            max_area = max(max_area, dist * container_ht) 
        
        return max_area

