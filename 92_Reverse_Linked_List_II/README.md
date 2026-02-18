# 92. Reverse Linked List II

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Linked List, Recursion

---

## Problem Description

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg)
```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```
Example 2:

```
Input: head = [5], left = 1, right = 1
Output: [5]
```

## Constraints

- The number of nodes in the list is `n`.0
- `1 <= n <= 500`
- `500 <= Node.val <= 500`
- `1 <= left <= right <= n`

---

## Approach 1: Recursion

### Intuition

`n` is the starting position to reverse the list. `m` is the ending position to reverse the list.

We can use recursion to reverse the nodes of the list from position `left` to position `right`. In the preorder traversal, we will move `left` and `right` to its corresponding positions in the list. In each recursion, we call the function with `n-1` and `m-1`.  In the postorder traversal, we will swap the `left` and `right` nodes and increment left by 1. 

### Complexity Analysis
Let `n` be the length of the list.
- **Time Complexity:** `O(n)`
    - During normal recursion, `O(n)` to move `left` and `right` to its corresponding positions in the list.
    - `O(n)` to swap the nodes.
- **Space Complexity:** `O(n)`
    - `O(n)` for the recursive call stack.


---

## Approach 2: Iteration

### Intuition

We can use iteration to reverse the nodes of the list from position `left` to position `right`. We first move both pointers to the right until we reach the start of the reversal position. We record the previous node of `curr` as `con`, and the `curr` node as `tail`. Then, for the remaining `m - n` nodes, we connect each node to the previous node and move `curr` to the next node. 
After the reversal, we connect `con` to the new head of the reversed list, and `tail` to the next node that is not in the reversed list.


### Complexity Analysis
Let `n` be the length of the list.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`


## Implementation

See `solution.py` for the full implementation.
