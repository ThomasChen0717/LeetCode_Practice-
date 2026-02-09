# Approach 1: Heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        heap = []
        for val, cnt in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, val))
            else:
                if cnt > heap[0][0]:
                    heapq.heapreplace(heap, (cnt, val))

        return [val for (cnt, val) in heap]

# Approach 2: Quick Select
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int: 
            store_idx = left 

            pivot_freq= count[unique[pivot_index]] 

            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            while left < right: 
                curr_freq = count[unique[left]]
                if curr_freq < pivot_freq: 
                    unique[left], unique[store_idx] = unique[store_idx], unique[left]
                    store_idx += 1
                left += 1

            unique[right], unique[store_idx] = unique[store_idx], unique[right]

            return store_idx

        def quickselect(left, right, k_smallest) -> None: 
            if left == right: return

            pivot_index = random.randint(left, right) 

            pivot_index = partition(left, right, pivot_index) 


            if k_smallest == pivot_index:
                 return 
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            else:
                quickselect(pivot_index + 1, right, k_smallest)
            
        n = len(unique) 

        quickselect(0, n - 1, n - k)

        return unique[n - k:]


        

