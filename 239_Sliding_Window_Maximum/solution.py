# Approach 1: Priority Queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = [] 
        deleted = {} 

        n = len(nums)

        res = []

        start = 0 
        
        for end in range(n): 
            heapq.heappush(max_heap, -nums[end]) 

            if end - start + 1 == k: 
                while max_heap and deleted.get(-max_heap[0], 0) > 0: 
                    deleted[-max_heap[0]] -= 1
                    heapq.heappop(max_heap) 

                res.append(-max_heap[0])

                out_val = nums[start]
                deleted[out_val] = deleted.get(out_val, 0) + 1
                start += 1
        
        return res

        
# Approach 2: Monotonic Queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque() 

        for i in range(k): 
            while q and nums[i] >= nums[q[-1]]: 
                q.pop() 
            q.append(i) 
        
        ans = [nums[q[0]]]
        for i in range(k, n): 
            while q and nums[i] >= nums[q[-1]]: 
                q.pop() 
            q.append(i) 

            while q[0] <= i - k: 
                q.popleft() 
            
            ans.append(nums[q[0]])
        
        return ans

# Approach 3: Block Separation + Prefix/Suffix Array
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefixMax, suffixMax = [0] * n, [0] * n
        for i in range(n):
            if i % k == 0:
                prefixMax[i] = nums[i]
            else:
                prefixMax[i] = max(prefixMax[i - 1], nums[i])
        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                suffixMax[i] = nums[i]
            else:
                suffixMax[i] = max(suffixMax[i + 1], nums[i])

        ans = [max(suffixMax[i], prefixMax[i + k - 1]) for i in range(n - k + 1)]
        return ans