# Approach 1: Quick Sort
class Solution:
    def compare(self, num1, num2): 
        return str(num1) + str(num2) > str(num2) + str(num1) 

    def partition(self, nums, lo, hi): 
        pivot = nums[hi]
        low_idx = lo 

        for i in range(lo, hi): 
            if self.compare(nums[i], pivot): 
                nums[i], nums[low_idx] = nums[low_idx], nums[i] 
                low_idx += 1
        
        nums[low_idx], nums[hi] = nums[hi], nums[low_idx]
        return low_idx 
    
    def quick_sort(self, nums, lo, hi): 
        if lo >= hi: 
            return 
        
        pivot = self.partition(nums, lo, hi)

        self.quick_sort(nums, lo, pivot - 1)
        self.quick_sort(nums, pivot + 1, hi)

    def largestNumber(self, nums: List[int]) -> str:
        self.quick_sort(nums, 0, len(nums) - 1)

        largest_num = "".join([str(num) for num in nums])

        return "0" if largest_num[0] == "0" else largest_num

# Approach 2: Merge Sort
class Solution:
    def compare(self, num1, num2): 
        return str(num1) + str(num2) > str(num2) + str(num1) 

    def merge(self, left, right): 
        sorted_list = [] 

        left_idx = 0
        right_idx = 0 

        while left_idx < len(left) and right_idx < len(right): 
            if self.compare(left[left_idx], right[right_idx]): 
                sorted_list.append(left[left_idx])
                left_idx += 1
            else: 
                sorted_list.append(right[right_idx])
                right_idx += 1
        
        while left_idx < len(left):
            sorted_list.append(left[left_idx])
            left_idx += 1
        
        while right_idx < len(right):
            sorted_list.append(right[right_idx])
            right_idx += 1
        
        return sorted_list
    
    def merge_sort(self, nums, lo, hi): 
        if lo >= hi: 
            return [nums[lo]]
        
        mid = lo + (hi - lo) // 2

        left = self.merge_sort(nums, lo, mid)
        right = self.merge_sort(nums, mid + 1, hi)

        return self.merge(left, right)

    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums = self.merge_sort(nums, 0, len(nums) - 1)

        largest_num = "".join([str(num) for num in sorted_nums])

        return "0" if largest_num[0] == "0" else largest_num

# Approach 3: Heap Sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"

        class LargerStrComparator(str):
            def __lt__(self, other):
                return self + other > other + self

        heap = []
        for num in nums:
            heapq.heappush(heap, LargerStrComparator(str(num)))

        result = []
        while heap:
            result.append(heapq.heappop(heap))

        largest_num = "".join(result)

        return "0" if largest_num[0] == "0" else largest_num
    

# Approach 4: Time Sort
class Solution:
    RUN = 32

    def largestNumber(self, nums: List[int]) -> str:
        # Sort the numbers using custom Tim Sort
        self.tim_sort(nums)
        # Concatenate sorted numbers to form the largest number
        largest_num = "".join(map(str, nums))
        # Handle the case where the largest number is zero
        return "0" if largest_num[0] == "0" else largest_num

    def insertion_sort(self, nums: List[int], left: int, right: int):
        for i in range(left + 1, right + 1):
            temp = nums[i]
            j = i - 1
            while j >= left and self.compare(temp, nums[j]):
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = temp

    def merge(self, nums: List[int], left: int, mid: int, right: int):
        left_arr = nums[left : mid + 1]
        right_arr = nums[mid + 1 : right + 1]

        i, j, k = 0, 0, left
        while i < len(left_arr) and j < len(right_arr):
            if self.compare(left_arr[i], right_arr[j]):
                nums[k] = left_arr[i]
                i += 1
            else:
                nums[k] = right_arr[j]
                j += 1
            k += 1
        nums[k : right + 1] = left_arr[i:] + right_arr[j:]

    def tim_sort(self, nums: List[int]):
        n = len(nums)
        # Sort small runs with insertion sort
        for i in range(0, n, self.RUN):
            self.insertion_sort(nums, i, min(i + self.RUN - 1, n - 1))
        # Merge sorted runs
        size = self.RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = left + size - 1
                right = min(left + 2 * size - 1, n - 1)
                if mid < right:
                    self.merge(nums, left, mid, right)
            size *= 2

    def compare(self, first_num: int, second_num: int) -> bool:
        return str(first_num) + str(second_num) > str(second_num) + str(
            first_num
        )