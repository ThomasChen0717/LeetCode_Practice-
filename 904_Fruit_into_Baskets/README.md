# 904. Fruit Into Baskets

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Sliding Window, Array

---

## Problem Description

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the `ith` tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

- You only have **two** baskets, and each basket can only hold a **single type** of fruit. There is no limit on the amount of fruit each basket can hold.
- Starting from any tree of your choice, you must pick **exactly one fruit** from **every** tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array `fruits`, return the **maximum** number of fruits you can pick.

---

## Examples
Example 1:
```
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
```
Example 2:
```
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
```
Example 3:
```
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
```
## Constraints

- `1 <= fruits.length <= 10^5`
- `0 <= fruits[i] < fruits.length`

---

## Approach 1: Brute Force Optimized

### Intuition

We iterate through the array and for each index `i`, we find the maximum number of fruits we can pick starting from `i`. When we reach a point with three different types of fruits, we stop and increment `i` to the next tree. 

### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Sliding Window

### Intuition

We keep a sliding window tracking the maximum number of fruits we can pick with two baskets. If the window contains more than two types of fruits, we continuously move the left pointer to the right until the window contains only two types of fruits. Keep track of the maximum number of fruits we can pick.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
