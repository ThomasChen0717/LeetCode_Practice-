# Approach 1: Binary Search 
class MedianFinder:

    def __init__(self):
        self.store = []

    def findPos(self, num: int): 
        left, right = 0, len(self.store)

        while left < right: 
            mid = left + (right - left) // 2
            if self.store[mid] < num: 
                left = mid + 1
            else:
                right = mid
        
        return left  
        

    def addNum(self, num: int) -> None:
        if len(self.store) == 0: 
            self.store.append(num)
        else: 
            pos = self.findPos(num)
            self.store.insert(pos, num) 


    def findMedian(self) -> float:
        n = len(self.store)
        return (self.store[n // 2 - 1] + self.store[n // 2]) * 0.5 if n % 2 == 0 else self.store[n // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Approach 2: Two Heaps
class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, num)

        heapq.heappush(self.hi, -heapq.heappop(self.lo)) 

        if len(self.lo) < len(self.hi): 
            heapq.heappush(self.lo, -heapq.heappop(self.hi))


    def findMedian(self) -> float:
        return self.lo[0] if len(self.hi) < len(self.lo) else (self.lo[0] - self.hi[0]) / 2

