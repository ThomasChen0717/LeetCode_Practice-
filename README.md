# LeetCode Practice Repository

This repository documents my LeetCode practice with a focus on **understanding**, not just solving.
Each solution is accompanied by notes explaining the reasoning, invariants, edge cases, and
complexity tradeoffs involved.

Problems are stored once and may be associated with multiple topics (e.g. Binary Search,
Two Pointers, Dynamic Programming). Topic overlap is documented explicitly in each problem’s README.

---

## Problem Index

| # | Problem | Reviews | Topics | Difficulty |
|---|--------|---------|--------|------------|
| 1 | Two Sum | 1 | Array, Hash Table | <span style="color:#2ecc71"><b>Easy</b></span> | 
| 2 | Add Two Numbers | 1 | Linked List, Math | <span style="color:#f39c12"><b>Medium</b></span> |
| 3 | Longest Substring Without Repeating Characters | 1 | String, Sliding Window | <span style="color:#f39c12"><b>Medium</b></span> |
| 4 | Median of Two Sorted Arrays | 1 | Array, Binary Search, Divide and Conquer | <span style="color:#e74c3c"><b>Hard</b></span> |
| 5 | Longest Palindromic Substring | 1 | String, Dynamic Programming, Expand Around Center | <span style="color:#f39c12"><b>Medium</b></span> |
| 6 | Zigzag Conversion | 0 | String | <span style="color:#f39c12"><b>Medium</b></span> |
| 7 | Reverse Integer | 0 | Math, digit manipulation | <span style="color:#f39c12"><b>Medium</b></span> |
| 9 | Palindrome Number | 1 | Math | <span style="color:#2ecc71"><b>Easy</b></span> |
| 11 | Container With Most Water | 1 | Array, Two Pointers | <span style="color:#f39c12"><b>Medium</b></span> |
| 14 | Longest Common Prefix | 1 | String, Array | <span style="color:#2ecc71"><b>Easy</b></span> |
| 15 | 3Sum | 1 | Array, Two Pointers, Sorting. Hash Map, Hash Set | <span style="color:#f39c12"><b>Medium</b></span> |
| 16 | 3Sum Closest | 0 | Array, Two Pointers, Sorting | <span style="color:#f39c12"><b>Medium</b></span> |
| 19 | Remove Nth Node From End of List | 0 | Linked List, Two Pointers | <span style="color:#f39c12"><b>Medium</b></span> |
| 20 | Valid Parentheses | 1 | String, Stack | <span style="color:#2ecc71"><b>Easy</b></span> |
| 31 | Next Permutation | 0 | Array, Math | <span style="color:#f39c12"><b>Medium</b></span> |
| 33 | Search in Rotated Sorted Array | 0 | Array, Binary Search | <span style="color:#f39c12"><b>Medium</b></span> |
| 34 | Find First and Last Position of Element in Sorted Array | 0 | Array, Binary Search | <span style="color:#f39c12"><b>Medium</b></span> |
| 40 | Combination Sum II | 0 | Array, Backtracking | <span style="color:#f39c12"><b>Medium</b></span> |
| 42 | Trapping Rain Water | 1 | Array, Two Pointers, Dynamic Programming, Stack | <span style="color:#e74c3c"><b>Hard</b></span> |
| 45 | Jump Game II | 0 | Array, Dynamic Programming, Greedy | <span style="color:#f39c12"><b>Medium</b></span> |
| 46 | Permutations | 0 | Array, Backtracking | <span style="color:#f39c12"><b>Medium</b></span> |
| 49 | Group Anagrams | 0 | Array, Hash Table, String, Sorting | <span style="color:#f39c12"><b>Medium</b></span> |
| 53 | Maximum Subarray | 1 | Array, Dynamic Programming, Divide and Conquer | <span style="color:#f39c12"><b>Medium</b></span> |
| 54 | Spiral Matrix | 0 | Matrix, DFS | <span style="color:#f39c12"><b>Medium</b></span> |
| 55 | Jump Game | 0 | Array, Dynamic Programming, Greedy | <span style="color:#f39c12"><b>Medium</b></span> |
| 56 | Merge Intervals | 1 | Array, Sorting, Graph | <span style="color:#f39c12"><b>Medium</b></span> |
| 66 | Plus One | 1 | Array, Math | <span style="color:#2ecc71"><b>Easy</b></span> |
| 72 | Edit Distance | 0 | String, Dynamic Programming, Recursion | <span style="color:#e74c3c"><b>Hard</b></span> |
| 75 | Sort Colors | 0 | Array, Sorting, Three Pointers | <span style="color:#f39c12"><b>Medium</b></span> |
| 78 | Subsets | 0 | Array, Backtracking, Bitmasking | <span style="color:#f39c12"><b>Medium</b></span> |
| 84 | Largest Rectangle in Histogram | 0 | Array, Stack | <span style="color:#e74c3c"><b>Hard</b></span> |
| 85 | Maximal Rectangle | 0 | Array, Dynamic Programming, Stack | <span style="color:#e74c3c"><b>Hard</b></span> |
| 92 | Reverse Linked List II | 0 | Linked List | <span style="color:#f39c12"><b>Medium</b></span> |
| 97 | Interleaving String | 0 | String, Dynamic Programming | <span style="color:#f39c12"><b>Medium</b></span> |
| 118 | Pascal's Triangle | 0 | Array, Dynamic Programming | <span style="color:#2ecc71"><b>Easy</b></span> |
| 121 | Best Time to Buy and Sell Stock | 1 | Array | <span style="color:#2ecc71"><b>Easy</b></span> |
| 128 | Longest Consecutive Sequence | 1 | Array, HashSet | <span style="color:#f39c12"><b>Medium</b></span> |
| 139 | Word Break | 0 | String, Dynamic Programming, Trie, Breadth-First Search | <span style="color:#f39c12"><b>Medium</b></span> |
| 146 | LRU Cache | 0 | Design, Hash Table, Doubly Linked List | <span style="color:#f39c12"><b>Medium</b></span> |
| 155 | Min Stack | 0 | Stack, Design | <span style="color:#f39c12"><b>Medium</b></span> |
| 162 | Find Peak Element | 0 | Array, Binary Search | <span style="color:#f39c12"><b>Medium</b></span> |
| 167 | Two Sum II - Input Array Is Sorted | 0 | Array, Two Pointers | <span style="color:#f39c12"><b>Medium</b></span> |
| 189 | Rotate Array | 0 | Array, Math, Two Pointers | <span style="color:#f39c12"><b>Medium</b></span> |
| 198 | House Robber | 0 | Dynamic Programming, Recursion, Memoization | <span style="color:#f39c12"><b>Medium</b></span> |
| 200 | Number of Islands | 0 | Graph, DFS, BFS, Union Find | <span style="color:#f39c12"><b>Medium</b></span> |
| 207 | Course Schedule | 0 | Graph, Topological Sort, DFS, BFS | <span style="color:#f39c12"><b>Medium</b></span> |
| 210 | Course Schedule II | 0 | Graph, Topological Sort, DFS, BFS | <span style="color:#f39c12"><b>Medium</b></span> |
| 215 | Kth Largest Element in an Array | 0 | Array, Sorting, Quick Select, Counting Sort | <span style="color:#f39c12"><b>Medium</b></span> |
| 236 | Lowest Common Ancestor of a Binary Tree | 0 | Binary Tree, DFS | <span style="color:#f39c12"><b>Medium</b></span> |
| 238 | Product of Array Except Self | 1 | Array, Prefix Sum | <span style="color:#f39c12"><b>Medium</b></span> |
| 242 | Valid Anagram | 1 | String, Sorting, Hash Table | <span style="color:#2ecc71"><b>Easy</b></span> |
| 249 | Group Shifted Strings | 0 | String, Hash Map | <span style="color:#f39c12"><b>Medium</b></span> |
| 253 | Meeting Rooms II | 0 | Heap, Sorting, Chronological Ordering | <span style="color:#f39c12"><b>Medium</b></span> |
| 268 | Missing Number | 0 | Array, Math, Bit Manipulation, Sorting, HashSet | <span style="color:#2ecc71"><b>Easy</b></span> |
| 300 | Longest Increasing Subsequence | 0 | Array, Dynamic Programming, Binary Search | <span style="color:#f39c12"><b>Medium</b></span> |
| 345 | Reverse Vowels of a String | 0 | String, Two Pointers | <span style="color:#2ecc71"><b>Easy</b></span> |
| 347 | Top K Frequent Elements | 0 | Array, Hash Table, Heap, Quick Select | <span style="color:#f39c12"><b>Medium</b></span> |
| 351 | Android Unlock Patterns | 0 | Backtracking, DP/Memoization | <span style="color:#f39c12"><b>Medium</b></span> |
| 359 | Logger Rate Limiter | 0 | Hash Table, Queue, Set | <span style="color:#2ecc71"><b>Easy</b></span> |
| 360 | Sort Transformed Array | 0 | Array, Math, Two Pointers | <span style="color:#f39c12"><b>Medium</b></span> |
| 394 | Decode String | 0 | String, Stack, Recursion | <span style="color:#f39c12"><b>Medium</b></span> |
| 415 | Add Strings | 0 | Math, String | <span style="color:#2ecc71"><b>Easy</b></span> | 
| 442 | Find All Duplicates in an Array | 0 | Array, Cyclic Sort | <span style="color:#f39c12"><b>Medium</b></span> |
| 443 | String Compression | 0 | Array, String, Math | <span style="color:#f39c12"><b>Medium</b></span> |
| 518 | Coin Change II | 0 | Dynamic Programming | <span style="color:#f39c12"><b>Medium</b></span> |
| 525 | Contiguous Array | 0 | Prefix Sum, HashMap | <span style="color:#f39c12"><b>Medium</b></span> |
| 560 | Subarray Sum Equals K | 1 | Array, Prefix Sum, HashMap | <span style="color:#f39c12"><b>Medium</b></span> |
| 658 | Find K Closest Elements | 0 | Binary Search, Sliding Window, Sorting | <span style="color:#f39c12"><b>Medium</b></span> |
| 678 | Valid Parenthesis String | 0 | Stack, Two Pointers, Dynamic Programming | <span style="color:#f39c12"><b>Medium</b></span> |
| 714 | Best Time to Buy and Sell Stock with Transaction Fee | 0 | Array, Dynamic Programming | <span style="color:#f39c12"><b>Medium</b></span> |
| 721 | Accounts Merge | 0 | Union Find, Graph, DFS | <span style="color:#f39c12"><b>Medium</b></span> |
| 728 | Self Dividing Numbers | 0 | Math, Brute Force | <span style="color:#2ecc71"><b>Easy</b></span> |
| 756 | Pyramid Transition Matrix | 0 | Backtracking, Dynamic Programming | <span style="color:#f39c12"><b>Medium</b></span> |
| 778 | Swim in Rising Water | 0 | Dijkstra's Algorithm | <span style="color:#e74c3c"><b>Hard</b></span> |
| 799 | Champagne Tower | 0 | Matrix, Simulation | <span style="color:#f39c12"><b>Medium</b></span> |
| 833 | Find And Replace in String | 0 | String, Sorting | <span style="color:#f39c12"><b>Medium</b></span> |
| 840 | Magic Squares in Grid | 0 | Array, Matrix, Simulation | <span style="color:#f39c12"><b>Medium</b></span> |
| 875 | Koko Eating Bananas | 1 | Array, Binary Search | <span style="color:#f39c12"><b>Medium</b></span> |
| 912 | Sort an Array | 0 | Array, Sorting | <span style="color:#f39c12"><b>Medium</b></span> |
| 944 | Delete Columns to Make Sorted | 0 | Array, String, Brute Force Matrix Traversal | <span style="color:#2ecc71"><b>Easy</b></span> |
| 977 | Squares of a Sorted Array | 0 | Array, Two Pointers, Sorting | <span style="color:#2ecc71"><b>Easy</b></span> |
| 1004 | Max Consecutive Ones III | 0 | Array, Sliding Window | <span style="color:#f39c12"><b>Medium</b></span> |
| 1143 | Longest Common Subsequence | 0 | Dynamic Programming, Memoization | <span style="color:#f39c12"><b>Medium</b></span> |
| 1161 | Maximum Level Sum of a Binary Tree | 0 | Binary Tree, BFS, DFS | <span style="color:#f39c12"><b>Medium</b></span> |
| 1244 | Design A Leaderboard | 0 | Hash Table, Heap(Priority Queue), TreeMap | <span style="color:#f39c12"><b>Medium</b></span> |
| 1339 | Maximum Product of Splitted Binary Tree | 0 | Bit Manipulation, Binary Tree, DFS | <span style="color:#f39c12"><b>Medium</b></span> |
| 1653 | Minimum Deletions to Make String Balanced | 0 | String, Dynamic Programming | <span style="color:#f39c12"><b>Medium</b></span> |
| 1877 | Minimize Maximum Pair Sum in Array | 0 | Array, Sorting | <span style="color:#f39c12"><b>Medium</b></span> |
| 1929 | Concatenation of Array | 1 | Array | <span style="color:#2ecc71"><b>Easy</b></span> |
| 1975 | Maximum Matrix Sum | 0 | Math | <span style="color:#f39c12"><b>Medium</b></span> |
| 2396 | Strictly Palindromic Number | 0 | Math | <span style="color:#f39c12"><b>Medium</b></span> |
| 2975 | Maximum Square Area by Removing Fences From a Field | 0 | Array, Math, Enumeration | <span style="color:#f39c12"><b>Medium</b></span> |
| 3074 | Apple Redistribution into Boxes | 0 | Array, Greedy | <span style="color:#2ecc71"><b>Easy</b></span> |
| 3453 | Separate Squares I | 0 | Array, Math, Sorting, Binary Search, Scan Line | <span style="color:#f39c12"><b>Medium</b></span> |









> Each problem links to a folder containing the final solution and a short write-up explaining the approach.