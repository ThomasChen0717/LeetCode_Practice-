# 19 Remove Nth Node From End Of List

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Two Pointers, Linked List

---

## Problem Description

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```
Example 2:
```
Input: head = [1], n = 1
Output: []
```
Example 3:

```
Input: head = [1,2], n = 1
Output: [1]
```

## Constraints

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

---

## Approach 1: Two Pass

### Intuition

Iterate through the list to find the length of the list. Then, iterate through the list again to find the node before the `nth` node from the end. Remove the `nth` node from the end. This is same as `length - n + 1`th node from the start. 

### Complexity Analysis
Let `n` be the number of nodes in the list.
- **Time Complexity:** `O(n)` 
- **Space Complexity:** `O(1)`

---

## Approach 2: One Pass

### Intuition

Use two pointers, `first` and `second`. Move `first` `n` steps ahead. Then, move `first` and `second` until `first` reaches the end of the list. `second` will be pointing to the node before the `nth` node from the end. Remove the `nth` node from the end.

### Complexity Analysis
- **Time Complexity:** `O(n)` 
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
