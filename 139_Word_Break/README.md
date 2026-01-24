# 139. Word Break

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Dynamic Programming, Breadth-First Search, Trie, String

---

## Problem Description

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.
---

## Examples
Example 1:
```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```
Example 2:
```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```
Example 3:
```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

## Constraints

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are **unique**.

---

## Approach 1: Breadth-First Search

### Intuition
We first create a set `words` from `wordDict` for faster lookup. 

Before the BFS loop, we append the index `0` to the queue. 

This index represents the starting point of the string `s`. 

For each index `start` in the queue, we check all possible substrings `s[start:end]` where `end` ranges from `start + 1` to `len(s) + 1`. 
If `s[start:end]` is in `wordDict`, we append `end` to the queue. 

We also mark `end` as visited to avoid revisiting it. 

When at any point in the search, if `start == len(s)`, we have found a valid segmentation. 
We return `True`.

If the queue becomes empty and we have not found a valid segmentation, we return `False`.

### Complexity Analysis
Let `n` be the length of the string `s`, `m` be the length of the `wordDict`, and `k` be the average length of the words in `wordDict`.
- **Time Complexity:** `O(n^3 + m * k)`
    - We have `n` nodes in total, because of the `seen` set, we visit each node at most once. 
        - Each node will process `n` nodes in front of it in the worst case. 
            - Each processing takes `O(n)` time due to string slicing. 
    - We also need `O(m * k)` time to create the set `words` from `wordDict`. 
        - This is because of string hashing. 
- **Space Complexity:** `O(n + m * k)`
    - We need `O(n)` space for the `seen` set. 
    - We also need `O(m * k)` space for the set `words`. 

---

## Approach 2: Top-Down Dynamic Programming

### Intuition
We first create a memo array `memo` of size `len(s)`, where `memo[i]` represents whether the substring `s[:i+1]` can be segmented into words from `wordDict`. 

We define a helper function `dp(idx)` that returns `True` if the substring `s[:idx+1]` can be segmented into words from `wordDict`, and `False` otherwise. 

In `dp(idx)`, we first check if `idx < 0`. 
If so, we return `True` because an empty string can always be segmented. 

If `memo[idx]` is not `-1`, we return `memo[idx] == 1` because `memo[idx]` stores the result of the subproblem `dp(idx)`. 

If `memo[idx]` is `-1`, we iterate through all words in `wordDict`. 
For each word `word`, we check if `s[idx - len(word) + 1:idx + 1] == word` and `dp(idx - len(word))` is `True`. 
If so, we set `memo[idx] = 1` and return `True`. 

If we have iterated through all words and not found a valid segmentation, we set `memo[idx] = 0` and return `False`.

### Complexity Analysis
Let `n` be the length of the string `s`, `m` be the length of the `wordDict`, and `k` be the average length of the words in `wordDict`.
- **Time Complexity:** `O(n * m * k)`
    - We have `n` nodes in total, because of the `memo` array, we visit each node at most once. 
        - Each node will process `m` words in `wordDict`.
            - Each processing takes `O(k)` time due to string slicing. 
- **Space Complexity:** `O(n)`
    - We need `O(n)` space for the `memo` array. 
    - We also need `O(n)` space for the recursive call stack. 

--- 

## Approach 3: Bottom-Up Dynamic Programming
The state definition is the same as the top-down approach. 
We define `dp[i]` as `True` if the substring `s[:i+1]` can be segmented into words from `wordDict`, and `False` otherwise. 

`dp` is set to `[False] * len(s)`. 

We do a special case handling, when `i - len(word) + 1 < 0`, means that the current word `word` is longer than the substring `s[:i+1]`. 
In this case, we skip this word. 

if `i == len(word) - 1`, then we don't have any `word` that can precede it. 
In this case, we just check if `word == s[i - len(word) + 1:i + 1]`. 
If so, we set `dp[i] = True`. 

We start from `i = 0`, and for each `i`, we iterate through all words in `wordDict`. 
For each word `word`, we check if `s[i - len(word) + 1:i + 1] == word` and `dp[i - len(word)]` is `True`. 
If so, we set `dp[i] = True` and break the loop. 


At the end, we return `dp[-1]`.

### Complexity Analysis
Let `n` be the length of the string `s`, `m` be the length of the `wordDict`, and `k` be the average length of the words in `wordDict`.
- **Time Complexity:** `O(n * m * k)`
    - We have `n` nodes in total, because of the `dp` array, we visit each node at most once. 
        - Each node will process `m` words in `wordDict`.
            - Each processing takes `O(k)` time due to string slicing. 
- **Space Complexity:** `O(n)`
    - We need `O(n)` space for the `dp` array. 

--- 

## Approach 4:  Optimized DP using Trie

### Intuition
We first create a Trie from `wordDict`. 
This Trie will be used to efficiently check if a substring of `s` is a word in `wordDict`. 0
The Trie stores `is_word` for each node, which indicates whether the node represents the end of a word in `wordDict`.  
We then do the bottom-up dynamic programming. 
We define `dp[i]` as `True` if the substring `s[:i+1]` can be segmented into words from `wordDict`, and `False` otherwise.  

### Complexity Analysis
Let `n` be the length of the string `s`, `m` be the length of the `wordDict`, and `k` be the average length of the words in `wordDict`.
- **Time Complexity:** `O(n * k + m * k)`
    - We have `n` nodes in total, because of the `dp` array, we visit each node at most once. 
        - Each node will process `k` characters 
            - Each processing takes `O(1)` time.
    - We also need `O(m * k)` time to create the Trie from `wordDict`. 
- **Space Complexity:** `O(n + m * k)`
    - We need `O(n)` space for the `dp` array. 
    - We also need `O(m * k)` space for the Trie. 

--- 

## Approach 5: A Different DP

### Intuition
We first create a set `words` from `wordDict`. 
We then do the bottom-up dynamic programming. 
We define `dp[i]` as `True` if it is possible to form `s up to a length of i` using words from `wordDict`.
The base case is `dp[0] = True`, because an empty string can always be created. 

We then iterate through all `i` from `1` to `n`. 
For each `i`, we iterate through all `j` from `0` to `i - 1`. 
If `dp[j]` is `True` and `s[j:i]` is in `words`, then we set `dp[i] = True` and break the loop. 


### Complexity Analysis
Let `n` be the length of the string `s`, `m` be the length of the `wordDict`, and `k` be the average length of the words in `wordDict`.
- **Time Complexity:** `O(n ^ 3 + m * k)`
    - We iterate over the length of `s` from `1` to `n`. 
        - For each `i`, we iterate over the length of `s` from `0` to `i - 1`. 
            - We process `s[j:i]` to check if it is in `words`, which takes `O(n)` in the worst case.
    - We also need `O(m * k)` time to create the set `words` from `wordDict`. 
- **Space Complexity:** `O(n + m * k)`
    - We need `O(n)` space for the `dp` array.
    - We also need `O(m * k)` space for the set `words` from `wordDict`.
See `solution.py` for the full implementation.
