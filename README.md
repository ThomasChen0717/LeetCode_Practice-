# LeetCode Practice Repository

This repository documents my LeetCode practice with a focus on **understanding**, not just solving.
Each solution is accompanied by notes explaining the reasoning, invariants, edge cases, and
complexity tradeoffs involved.

Problems are stored once and may be associated with multiple topics (e.g. Binary Search,
Two Pointers, Dynamic Programming). Topic overlap is documented explicitly in each problem’s README.

---

## Problem Index

| # | Problem | Topics | Difficulty |
|---|--------|--------|------------|
| 1 | Two Sum | Array, Hash Table | <span style="color:#2ecc71"><b>Easy</b></span> |
| 2 | Add Two Numbers | Linked List, Math | <span style="color:#f39c12"><b>Medium</b></span> |
| 3 | Longest Substring Without Repeating Characters | String, Sliding Window | <span style="color:#f39c12"><b>Medium</b></span> |
| 4 | Median of Two Sorted Arrays | Array, Binary Search, Divide and Conquer | <span style="color:#e74c3c"><b>Hard</b></span> |
| 5 | Longest Palindromic Substring | String, Dynamic Programming, Expand Around Center | <span style="color:#f39c12"><b>Medium</b></span> |
| 6 | Zigzag Conversion | String | <span style="color:#f39c12"><b>Medium</b></span> |
| 7 | Reverse Integer | Math, digit manipulation | <span style="color:#f39c12"><b>Medium</b></span> |
| 11 | Container With Most Water | Array, Two Pointers | <span style="color:#f39c12"><b>Medium</b></span> |
| 15 | 3Sum | Array, Two Pointers, Sorting. Hash Map, Hash Set | <span style="color:#f39c12"><b>Medium</b></span> |
| 19 | Remove Nth Node From End of List | Linked List, Two Pointers | <span style="color:#f39c12"><b>Medium</b></span> |
| 31 | Next Permutation | Array, Math | <span style="color:#f39c12"><b>Medium</b></span> |
| 33 | Search in Rotated Sorted Array | Array, Binary Search | <span style="color:#f39c12"><b>Medium</b></span> |
| 34 | Find First and Last Position of Element in Sorted Array | Array, Binary Search | <span style="color:#f39c12"><b>Medium</b></span> |
| 40 | Combination Sum II | Array, Backtracking | <span style="color:#f39c12"><b>Medium</b></span> |
| 42 | Trapping Rain Water | Array, Two Pointers, Dynamic Programming, Stack | <span style="color:#e74c3c"><b>Hard</b></span> |
| 45 | Jump Game II | Array, Dynamic Programming, Greedy | <span style="color:#f39c12"><b>Medium</b></span> |
| 46 | Permutations | Array, Backtracking | <span style="color:#f39c12"><b>Medium</b></span> |
| 54 | Spiral Matrix |  Matrix, DFS | <span style="color:#f39c12"><b>Medium</b></span> |
| 55 | Jump Game | Array, Dynamic Programming, Greedy | <span style="color:#f39c12"><b>Medium</b></span> |
| 56 | Merge Intervals | Array, Sorting, Graph | <span style="color:#f39c12"><b>Medium</b></span> |
| 72 | Edit Distance | String, Dynamic Programming, Recursion | <span style="color:#e74c3c"><b>Hard</b></span> |
| 75 | Sort Colors | Array, Sorting, Three Pointers | <span style="color:#f39c12"><b>Medium</b></span> |
| 78 | Subsets | Array, Backtracking, Bitmasking | <span style="color:#f39c12"><b>Medium</b></span> |
| 118 | Pascal's Triangle | Array, Dynamic Programming | <span style="color:#2ecc71"><b>Easy</b></span> |
| 121 | Best Time to Buy and Sell Stock | Array | <span style="color:#2ecc71"><b>Easy</b></span> |
| 128 | Longest Consecutive Sequence | Array, HashSet | <span style="color:#f39c12"><b>Medium</b></span> |
| 139 | Word Break | String, Dynamic Programming, Trie, Breadth-First Search | <span style="color:#f39c12"><b>Medium</b></span> |
| 146 | LRU Cache | Design, Hash Table, Doubly Linked List | <span style="color:#f39c12"><b>Medium</b></span> |
| 167 | Two Sum II - Input Array Is Sorted | Array, Two Pointers | <span style="color:#f39c12"><b>Medium</b></span> |
| 189 | Rotate Array | Array, Math, Two Pointers | <span style="color:#f39c12"><b>Medium</b></span> |
| 198 | House Robber | Dynamic Programming, Recursion, Memoization | <span style="color:#f39c12"><b>Medium</b></span> |
| 210 | Course Schedule II | Graph, Topological Sort, DFS, BFS | <span style="color:#f39c12"><b>Medium</b></span> |
| 215 | Kth Largest Element in an Array | Array, Sorting, Quick Select, Counting Sort | <span style="color:#f39c12"><b>Medium</b></span> |
| 236 | Lowest Common Ancestor of a Binary Tree | Binary Tree, DFS | <span style="color:#f39c12"><b>Medium</b></span> |
| 253 | Meeting Rooms II | Heap, Sorting, Chronological Ordering | <span style="color:#f39c12"><b>Medium</b></span> |
| 345 | Reverse Vowels of a String | String, Two Pointers | <span style="color:#2ecc71"><b>Easy</b></span> |
| 351 | Android Unlock Patterns | Backtracking, DP/Memoization | <span style="color:#f39c12"><b>Medium</b></span> |
| 359 | Logger Rate Limiter | Hash Table, Queue, Set | <span style="color:#2ecc71"><b>Easy</b></span> |
| 394 | Decode String | String, Stack, Recursion | <span style="color:#f39c12"><b>Medium</b></span> |
| 415 | Add Strings | Math, String | <span style="color:#2ecc71"><b>Easy</b></span> | 
| 443 | String Compression | Array, String, Math | <span style="color:#f39c12"><b>Medium</b></span> |
| 518 | Coin Change II | Dynamic Programming | <span style="color:#f39c12"><b>Medium</b></span> |
| 525 | Contiguous Array | Prefix Sum, HashMap | <span style="color:#f39c12"><b>Medium</b></span> |
| 560 | Subarray Sum Equals K | Array, Prefix Sum, HashMap | <span style="color:#f39c12"><b>Medium</b></span> |
| 658 | Find K Closest Elements | Binary Search, Sliding Window, Sorting | <span style="color:#f39c12"><b>Medium</b></span> |
| 678 | Valid Parenthesis String | Stack, Two Pointers, Dynamic Programming | <span style="color:#f39c12"><b>Medium</b></span> |
| 728 | Self Dividing Numbers | Math, Brute Force | <span style="color:#2ecc71"><b>Easy</b></span> |
| 756 | Pyramid Transition Matrix | Backtracking, Dynamic Programming | <span style="color:#f39c12"><b>Medium</b></span> |
| 778 | Swim in Rising Water | Dijkstra's Algorithm | <span style="color:#e74c3c"><b>Hard</b></span> |
| 840 | Magic Squares in Grid | Array, Matrix, Simulation | <span style="color:#f39c12"><b>Medium</b></span> |
| 875 | Koko Eating Bananas | Array, Binary Search | <span style="color:#f39c12"><b>Medium</b></span> |
| 912 | Sort an Array | Array, Sorting | <span style="color:#f39c12"><b>Medium</b></span> |
| 944 | Delete Columns to Make Sorted | Array, String, Brute Force Matrix Traversal | <span style="color:#2ecc71"><b>Easy</b></span> |
| 977 | Squares of a Sorted Array | Array, Two Pointers, Sorting | <span style="color:#2ecc71"><b>Easy</b></span> |
| 1004 | Max Consecutive Ones III | Array, Sliding Window | <span style="color:#f39c12"><b>Medium</b></span> |
| 1143 | Longest Common Subsequence | Dynamic Programming, Memoization | <span style="color:#f39c12"><b>Medium</b></span> |
| 1161 | Maximum Level Sum of a Binary Tree | Binary Tree, BFS, DFS | <span style="color:#f39c12"><b>Medium</b></span> |
| 1244 | Design A Leaderboard | Hash Table, Heap(Priority Queue), TreeMap | <span style="color:#f39c12"><b>Medium</b></span> |
| 1339 | Maximum Product of Splitted Binary Tree | Bit Manipulation, Binary Tree, DFS | <span style="color:#f39c12"><b>Medium</b></span> |
| 1975 | Maximum Matrix Sum | Math | <span style="color:#f39c12"><b>Medium</b></span> |
| 2396 | Strictly Palindromic Number | Math | <span style="color:#f39c12"><b>Medium</b></span> |
| 2975 | Maximum Square Area by Removing Fences From a Field | Array, Math, Enumeration | <span style="color:#f39c12"><b>Medium</b></span> |
| 3074 | Apple Redistribution into Boxes | Array, Greedy | <span style="color:#2ecc71"><b>Easy</b></span> |
| 3453 | Separate Squares I | Array, Math, Sorting, Binary Search, Scan Line | <span style="color:#f39c12"><b>Medium</b></span> |









> Each problem links to a folder containing the final solution and a short write-up explaining the approach.