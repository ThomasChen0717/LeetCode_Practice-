# Approach 1: Brute Force
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        size = len(height)

        for i in range(1, size - 1): 
            left_max = 0
            right_max = 0 

            for j in range(i+1):
                left_max = max(left_max, height[j]) 
            
            for j in range(size - 1, i - 1, -1): 
                right_max = max(right_max, height[j]) 
            
            ans += min(left_max, right_max) - height[i]
        
        return ans
            
#Approach 2: Dynamic Programming
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        size = len(height)

        left_max = [0] * size 
        right_max = [0] * size 


        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[size-1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for i in range(1, size-1): 
            ans += min(left_max[i], right_max[i]) - height[i] 
        return ans 
        
#Appraoch 3: Stack 
class Solution:
    def trap(self, height: List[int]) -> int:
        st = [] 
        ans = 0 
        n = len(height)
        curr = 0

        while curr < n: 
            while st and height[curr] > height[st[-1]]: 
                top = st.pop() 
                if len(st) == 0: break 
                distance = curr - st[-1] - 1
                bounded_height = (
                    min(height[curr], height[st[-1]]) - height[top]
                )
                ans += distance * bounded_height

            st.append(curr)
            curr += 1
        return ans

#Approach 4: Two Pointers 
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0 
        n = len(height)

        left = 0
        right = n - 1

        left_max, right_max = 0, 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans



    