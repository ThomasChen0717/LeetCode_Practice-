# 1244. Design A Leaderboard

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Hash Table, Heap, SortedMap, TreeMap

---

## Problem Description

Design a Leaderboard class, which has 3 functions:

1. `addScore(playerId, score)`: Update the leaderboard by adding `score` to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given `score`.
1.  `top(K)`: Return the score sum of the top `K` players.
1. `reset(playerId)`: Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.

Initially, the leaderboard is empty.

---

## Examples
Example 1:
```
Input: 
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
Output: 
[null,null,null,null,null,null,73,null,null,null,141]

Explanation: 
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
```

## Constraints

- `1 <= playerId, K <= 10000`
- It's guaranteed that `K` is less than or equal to the current number of players.
- `1 <= score <= 100`
- There will be at most `1000` function calls.

---

## Approach 1: Hashmap 

### Intuition

Simply use a hashmap to store the score of each player. When we need top `K` players, we can sort the hashmap by score in descending order and return the sum of the first `K` players.

### Complexity Analysis

- **Time Complexity:** 
    - `O(1)` for `addScore`
    - `O(N log N)` for `top(K)` where `N` is the number of players
    - `O(1)` for `reset`
- **Space Complexity:** `O(N)`

---
## Approach 2: Hashmap + Heap for top(K)

### Intuition

Use a hashmap to store the score of each player. When we need top `K` players, we can use a min heap to store the top `K` players. We can maintain the heap by adding the score of each player to the heap. If the heap size exceeds `K`, we can remove the smallest score from the heap. Finally, we can return the sum of the scores in the heap.

### Complexity Analysis

- **Time Complexity:** 
    - `O(1)` for `addScore`
    - `O(N log K)` for `top(K)` where `N` is the number of players and `K` is the number of top players to return
    - `O(1)` for `reset`
- **Space Complexity:** `O(N + K)`

## Approach 3: Hashmap + SortedMap for top(K)

### Intuition

Maintain a sorted map (TreeMap in Java) to store the score of each player. When we need top `K` players, we can return the sum of the last `K` players in the sorted map. Keep a frequency of each score for efficient removal when resetting a player.

### Complexity Analysis
`N` is the number of players
- **Time Complexity:** 
    - `O(log N)` for `addScore`
    - `O(K)` for `top(K)` where `K` is the number of top players to return
    - `O(log N)` for `reset`
- **Space Complexity:** `O(N)`
## Implementation

See `solution.py` for the full implementation.
