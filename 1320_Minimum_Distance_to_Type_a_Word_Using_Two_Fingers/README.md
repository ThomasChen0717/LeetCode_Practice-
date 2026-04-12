# 1320. Minimum Distance to Type a Word Using Two Fingers

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** Dynamic Programming

---

## Problem Description

You have a keyboard layout as shown in the problem description, where each English uppercase letter is located at some coordinate. You are given a string `word` and you need to type it using two fingers. The distance between two coordinates is the Manhattan distance.

The initial positions of your two fingers are free, so they do not count towards the total distance. Your two fingers do not have to start at the first letter or the first two letters.

Return the minimum total distance to type the given `word`.

---

## Examples

**Example 1:**
```
Input: word = "CAKE"
Output: 3
```
**Explanation:**
One optimal way to type "CAKE" is:
- Finger 1 on 'C' -> cost = 0
- Finger 1 on 'A' -> cost = Distance('C', 'A') = 2
- Finger 2 on 'K' -> cost = 0
- Finger 2 on 'E' -> cost = Distance('K', 'E') = 1
Total distance = 3

**Example 2:**
```
Input: word = "HAPPY"
Output: 6
```
**Explanation:**
One optimal way to type "HAPPY" is:
- Finger 1 on 'H' -> cost = 0
- Finger 1 on 'A' -> cost = Distance('H', 'A') = 2
- Finger 2 on 'P' -> cost = 0
- Finger 2 on 'P' -> cost = Distance('P', 'P') = 0
- Finger 1 on 'Y' -> cost = Distance('A', 'Y') = 4
Total distance = 6

## Constraints

- `2 <= word.length <= 300`
- `word` consists of uppercase English letters.

---

## Approach: Space Optimized Dynamic Programming

### Intuition

This problem can be solved using dynamic programming. At each step of typing the word, the state can be defined by the positions of the two fingers. Let's say we are at character `i` of the word, and our fingers are on characters `f1` and `f2`.

Let `dp[f1][f2]` be the minimum cost to have typed the word up to a certain point, with one finger at position `f1` and the other at `f2`. When we move to the next character in the word, say `c`, we have two choices:
1. Move the first finger from `f1` to `c`. The new state will be `(c, f2)` and the cost will be the original cost plus the distance from `f1` to `c`.
2. Move the second finger from `f2` to `c`. The new state will be `(f1, c)` and the cost will be the original cost plus the distance from `f2` to `c`.

We want to take the minimum of these two choices for each possible next state.

The initial positions of the fingers are "free". We can model this by considering the fingers to be at a virtual location with a distance of 0 to any character on the keyboard for the first move.

The provided solution implements this with a space-optimized DP. It uses a dictionary `dp` to store the current states `(f1, f2)` and their associated minimum costs. It iterates through each character of the input `word`. In each iteration, it computes a `new_dp` dictionary for the new character based on the states in `dp` from the previous character. After computing all possible new states, `dp` is updated to `new_dp` for the next iteration.

The `dist(a, b)` helper function calculates the Manhattan distance between two characters, represented as numbers from 0 to 25. A special value (`-1` in the solution) is used to represent the initial "free" position of a finger.

After iterating through all characters in the word, the minimum value among all values in the final `dp` dictionary will be the minimum total distance to type the word.

### Complexity Analysis

- **Time Complexity:** `O(N * C^2)`, where `N` is the length of the word and `C` is the number of characters in the alphabet (26). For each character in the word, we iterate through all possible previous states. The number of states is at most `C*C`. Since `C` is a constant (26), the complexity is effectively `O(N)`.
- **Space Complexity:** `O(C^2)`. The space used by the `dp` dictionary is proportional to the number of states, which is at most `C*C`. Since `C` is constant, this is `O(1)`.

---

## Implementation

See `solution.py` for the full implementation.
