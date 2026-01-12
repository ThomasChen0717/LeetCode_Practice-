# 2. Add Two Numbers

**Difficulty:** <span style="color:#2ecc71"><b>Medium</b></span>  
**Topics:** = Linked List, Math  

---

## Problem Description

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
---

## Examples
Example 1:
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```
Example 2:
```
Input: l1 = [0], l2 = [0]
Output: [0]
```
Example 3:
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

---

## Approach: Math

### Intuition
To add two numbers represented by linked lists, we can treat each node as a digit of a number. We start from the head of each list and move towards the tail, adding the corresponding digits along with any carry from the previous addition.

### Complexity Analysis

- **Time Complexity:** `O(max(m, n))`, where `m` and `n` are the lengths of the two input linked lists.
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
