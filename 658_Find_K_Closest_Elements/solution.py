# Approach 1: Sorting
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sort using custom comparator
        sorted_arr = sorted(arr, key = lambda num: abs(x - num))

        # Only take k elements
        result = []
        for i in range(k):
            result.append(sorted_arr[i])
        
        # Sort again to have output in ascending order
        return sorted(result)

#Approach 2: Binary Search + Sliding Window
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr 

        
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        left, right = right, left

        while right - left - 1 < k: 
            if left == -1: 
                right += 1
                continue 
            
            if right == len(arr): 
                left -= 1
                continue 
            
            if abs(arr[left] - x) <= abs(arr[right] - x): 
                left -= 1
            else: 
                right += 1
            
        return arr[left + 1: right]

# Approach 3: Binary Search 
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k 

        while left < right: 
            mid = left + (right - left) // 2
            if x - arr[mid] <= arr[mid + k] - x: 
                right = mid
            else: 
                left = mid + 1
        
        return arr[left:left+k]
            