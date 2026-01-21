# Approach 1: Merge Sort 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp_arr = [0] * len(nums)
        def merge(lo, mid, hi): 
            start1 = lo 
            start2 = mid + 1

            len1 = mid - lo + 1
            len2 = hi - mid

            for i in range(start1, mid + 1): 
                temp_arr[i] = nums[i] 
            for j in range(start2, hi + 1): 
                temp_arr[j] = nums[j] 
            
            i,j,k = 0,0,lo 

            while i < len1 and j < len2: 
                if temp_arr[start1 + i] <= temp_arr[start2 + j]: 
                    nums[k] = temp_arr[start1 + i]
                    i += 1
                else: 
                    nums[k] = temp_arr[start2 + j] 
                    j += 1
                k += 1
            
            while i < len1: 
                nums[k] = temp_arr[start1 + i] 
                i += 1
                k += 1
            
            while j < len2:
                nums[k] = temp_arr[start2 + j]
                j += 1
                k += 1
        
        def merge_sort(lo, hi): 
            if lo == hi: return 
            mid = lo + (hi - lo) // 2
            merge_sort(lo, mid) 
            merge_sort(mid + 1, hi) 

            merge(lo, mid, hi) 

        merge_sort(0, len(nums) - 1)
        return nums
    
# Approach 2: Heap Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(n, i): 
            largest = i 
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and nums[left] > nums[largest]: 
                largest = left 
            if right < n and nums[right] > nums[largest]: 
                largest = right 
            
            if largest != i: 
                nums[i], nums[largest] = nums[largest], nums[i] 
                heapify(n, largest)
        
        def heap_sort():
            n = len(nums)
            for i in range(n // 2 - 1, -1, -1):
                heapify(n, i)
            for i in range(n - 1, -1, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(i, 0)

        heap_sort()
        return nums

# Approach 3: Counting Sort 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = {} 

        min_val = float("inf")
        max_val = float("-inf")

        for val in nums: 
            count[val] = count.get(val, 0) + 1
            min_val = min(min_val, val) 
            max_val = max(max_val, val) 

        idx = 0 

        for i in range(min_val, max_val + 1): 
            if i in count: 
                while count[i] > 0: 
                    nums[idx] = i 
                    idx += 1 
                    count[i] -= 1
        
        return nums

# Approach 4: Radix Sort 
class Solution:
    # Radix sort function.
    def radix_sort(self, nums: List[int]) -> List[int]:
        # Find the absolute maximum element to find max number of digits.
        max_element = nums[0]
        for val in nums:
            max_element = max(abs(val), max_element)

        max_digits = 0
        while max_element > 0:
            max_digits += 1
            max_element = max_element // 10

        place_value = 1
        
        # Bucket sort function for each place value digit.
        def bucket_sort():
            buckets = [[] for i in range(10)]
            # Store the respective number based on it's digit.
            for val in nums:
                digit = abs(val) / place_value
                digit = int(digit % 10)
                buckets[digit].append(val)

            # Overwrite 'nums' in sorted order of current place digits.
            index = 0
            for digit in range(10):
                for val in buckets[digit]:
                    nums[index] = val
                    index += 1

        # Radix sort, least significant digit place to most significant.      
        for _ in range(max_digits):
            bucket_sort()
            place_value *= 10

        # Seperate out negatives and reverse them. 
        positives = [val for val in nums if val >= 0]
        negatives = [val for val in nums if val < 0]
        negatives.reverse()

        # Final 'arr' will be 'negative' elements, then 'positive' elements.
        return negatives + positives
            
    def sortArray(self, nums: List[int]) -> List[int]:  
        return self.radix_sort(nums)                                                      