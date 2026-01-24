# Approach 1: Binary Search for pivot and two binary searches on the two halves
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi: 
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[-1]: 
                lo = mid + 1
            else: 
                hi = mid 
            
        def binarySearch(left_bound, right_bound, target): 
            lo, hi = left_bound, right_bound 
            while lo <= hi: 
                mid = lo + (hi - lo) // 2
                if nums[mid] < target: 
                    lo = mid + 1
                elif nums[mid] >  target: 
                    hi = mid - 1
                else: 
                    return mid 
            return -1
        
        ans = binarySearch(0, lo - 1, target) 
        if ans != -1: return ans 

        return binarySearch(lo, len(nums) - 1, target)

# Approach 2: Find pivot + index shifted binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # Find the index of the pivot element (the smallest element)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        # Shift elements in circular manner, with the pivot element at index 0.
        # Then perform a regular binary search
        def shiftedBinarySearch(pivot_index, target):
            shift = n - pivot_index
            left, right = (pivot_index + shift) % n, (
                pivot_index - 1 + shift
            ) % n

            while left <= right:
                mid = (left + right) // 2
                if nums[(mid - shift) % n] == target:
                    return (mid - shift) % n
                elif nums[(mid - shift) % n] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        return shiftedBinarySearch(left, target)

# Approach 3: Single Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi: 
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] >= nums[lo]: 
                if target >= nums[lo] and nums[mid] > target: 
                    hi = mid - 1
                else: 
                    lo = mid + 1
            else: 
                if target > nums[mid] and nums[hi] >= target: 
                    lo = mid + 1
                else: 
                    hi = mid - 1

        
        return -1