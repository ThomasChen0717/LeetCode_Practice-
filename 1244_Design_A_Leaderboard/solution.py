#Approach 1: Hash Map 
class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:  
        if playerId not in self.scores: 
            self.scores[playerId] = 0
        self.scores[playerId] += score 


    def top(self, K: int) -> int:
        values = [v for _, v in sorted(self.scores.items(), key=lambda item: item[1])]
        values.sort(reverse=True)
        total, i = 0, 0
        while i < K:
            total += values[i]
            i += 1
        
        return total

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


#Approach 2: min heap for top-K
class Leaderboard:

    def __init__(self):
        self.scores = {}
        

    def addScore(self, playerId: int, score: int) -> None:  
        if playerId not in self.scores: 
            self.scores[playerId] = 0
        self.scores[playerId] += score 


    def top(self, K: int) -> int:
        heap = []
        for x in self.scores.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0

#Approach 3: Tree Map/SortedMap
class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict() 


    def addScore(self, playerId: int, score: int) -> None:  
        if playerId not in self.scores: 
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else: 
            preScore = self.scores[playerId] 
            val = self.sortedScores.get(-preScore) 
            if val == 1: 
                del self.sortedScores[-preScore]
            else: 
                self.sortedScores[-preScore] = val - 1    
            newScore = preScore + score 
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1
            self.scores[playerId] = newScore


    def top(self, K: int) -> int:
        count, total = 0,0

        for key, value in self.sortedScores.items(): 
            times = self.sortedScores.get(key)
            for _ in range(times): 
                total +=-key 
                count += 1

                if count == K: 
                    break 
            
            if count == K: 
                break 
        
        return total

    def reset(self, playerId: int) -> None:
        preScore = self.scores[playerId]
        if self.sortedScores[-preScore] == 1:
            del self.sortedScores[-preScore]
        else:
            self.sortedScores[-preScore] -= 1
        del self.scores[playerId]

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)