# Approach 1: Sorting + Min Heap

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        
        intervals.sort(key=lambda x: x[0])

        free_rooms = [] 

        heapq.heappush(free_rooms, intervals[0][1])

        for i in intervals[1:]: 
            if free_rooms[0] <= i[0]: 
                heapq.heappop(free_rooms) 
            
            heapq.heappush(free_rooms, i[1]) 

        
        return len(free_rooms)


# Approach 2: Chronological Ordering
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0

        used_rooms = 0

        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)

        s_end = 0 
        e_end = 0 

        while s_end < len(intervals): 
            if start_times[s_end] >= end_times[e_end]:
                e_end += 1 
                used_rooms -= 1
            s_end += 1
            used_rooms += 1
        
        return used_rooms 