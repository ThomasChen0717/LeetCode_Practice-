# Approach 1: Breadth-First Search
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        queue = deque([0]) 
        seen = set() 

        while queue: 
            start = queue.popleft() 
            if start == len(s): return True 

            for end in range(start + 1, len(s) + 1): 
                if end not in seen: 
                    substr = s[start:end] 
                    if substr in words: 
                        queue.append(end) 
                        seen.add(end) 
            
        return False

# Approach 2: Top-Down Dynamic Programming
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [-1] * len(s) 

        def dp(idx): 
            if idx < 0: return True 

            if memo[idx] != -1: return memo[idx] == 1

            for word in wordDict: 
                start = idx - len(word) + 1
                if start >= 0 and s[start:idx + 1] == word and dp(idx - len(word)): 
                    memo[idx] = 1
                    return True
            
            memo[idx] = 0
            return False 
        
        return dp(len(s) - 1)

# Approach 3: Bottom-Up Dynamic Programming
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) 

        for i in range(len(s)): 
            for word in wordDict: 
                if i - len(word) + 1 < 0: continue

                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1 : i + 1] == word:
                        dp[i] = True
                        break
        
        return dp[-1]

# Approach 4:  Optimized DP using Trie
class TrieNode: 
    def __init__(self): 
        self.is_word = False 
        self.children = {} 


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode() 

        for word in wordDict: 
            curr = root
            for c in word: 
                if c not in curr.children: 
                    curr.children[c] = TrieNode() 
                curr = curr.children[c] 
            
            curr.is_word = True


        dp = [False] * len(s) 

        for i in range(len(s)): 
            if i == 0 or dp[i-1]: 
                curr = root 
                for j in range(i, len(s)): 
                    c = s[j] 
                    if c not in curr.children: 
                        break 
                    
                    curr = curr.children[c]

                    if curr.is_word: 
                        dp[j] = True
        
        return dp[-1]

## Approach 5: A Different DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]