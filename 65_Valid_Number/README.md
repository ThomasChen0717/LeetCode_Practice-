# 65. Valid Number

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** String, Finite Automata

---

## Problem Description

A **valid number** can be described by the following rules:
- It can be an **integer** or a **decimal**.
- An **integer** has an optional sign `'+'` or `'-'` followed by one or more digits.
- A **decimal** has an optional sign `'+'` or `'-'` followed by one of the following:
  - One or more digits, followed by a dot `.`.
  - One or more digits, followed by a dot `.`, followed by one or more digits.
  - A dot `.`, followed by one or more digits.
- A number can be followed by an **exponent**, which consists of the character `'e'` or `'E'`, an optional sign, and one or more digits.

Given a string `s`, return `true` if `s` can be interpreted as a valid number, and `false` otherwise.

---

## Examples

**Example 1:**
`Input: s = "0"`
`Output: true`

**Example 2:**
`Input: s = "e"`
`Output: false`

**Example 3:**
`Input: s = "."`
`Output: false`

**Example 4:**
`Input: s = "2e10"`
`Output: true`

**Example 5:**
`Input: s = "-90E3"`
`Output: true`

**Example 6:**
`Input: s = "3.14"`
`Output: true`

**Invalid Numbers:** `"abc"`, `"1a"`, `"1e"`, `"e3"`, `"99e2.5"`, `"--6"`, `"-+3"`

## Constraints

- `1 <= s.length <= 20`
- `s` consists of only English letters (both uppercase and lowercase), digits (`0-9`), plus `'+'`, minus `'-'`, or dot `'.'`. 

---

## Approach 1: Follow the Rules (Iterative)

### Intuition

This approach involves iterating through the string and using a set of boolean flags to keep track of the components of a valid number that we have seen so far. The flags help enforce the rules of what constitutes a valid number.

The main flags are:
- `seen_digit`: Becomes true if we have seen at least one digit.
- `seen_exponent`: Becomes true if we have seen an 'e' or 'E'.
- `seen_dot`: Becomes true if we have seen a '.'.

We iterate through the string character by character and apply the following logic:
- **Digit:** If the character is a digit, we set `seen_digit = true`.
- **Sign (`+` or `-`):** A sign is only valid at the very beginning of the string or immediately after an 'e' or 'E'.
- **Dot (`.`):** A dot is invalid if we have already seen a dot or an exponent.
- **Exponent (`e` or `E`):** An exponent is invalid if we have already seen one or if we haven't seen any digits yet. After seeing an exponent, we reset `seen_digit` to `false` because the part after the 'e' must be a valid integer.
- **Other characters:** Any other character makes the string invalid.

After the loop, the string represents a valid number only if `seen_digit` is true. This final check is crucial for cases like `"e"` or `"1e"` where the part after the exponent is missing.

### Complexity Analysis

- **Time Complexity:** `O(N)`, where `N` is the length of the string `s`. We perform a single pass through the string.
- **Space Complexity:** `O(1)`. We only use a few boolean flags, which is constant extra space.

---

## Approach 2: Deterministic Finite Automaton (DFA)

### Intuition

The problem of validating a number can be modeled perfectly using a Deterministic Finite Automaton (DFA), also known as a state machine. A DFA consists of a set of states and transitions between them based on the input characters.

We can define a set of states that represent the parsing progress of the number:
- State 0: Initial state (can accept sign, digit, or dot).
- State 1: Seen digits (can accept more digits, a dot, or an exponent).
- State 2: Seen a sign at the beginning.
- State 3: Seen a dot at the beginning.
- State 4: Seen digits after a dot.
- State 5: Seen an exponent 'e'.
- State 6: Seen digits after an exponent.
- State 7: Seen a sign after an exponent.

We start in the initial state (State 0). For each character in the input string, we determine its type (digit, sign, dot, exponent) and transition to the next state based on our DFA definition. If at any point a character does not correspond to a valid transition from the current state, the string is invalid.

After processing the entire string, we check if the final state is one of the valid "accept" states. In this model, the accept states are those that represent a complete, valid number (e.g., states where we have seen at least one digit and are not in an intermediate state that requires more input, like just after an 'e'). The valid final states in the provided solution are 1, 4, and 6.

This approach is clean and robust, as it systematically handles all the rules through a well-defined state transition table.

### Complexity Analysis

- **Time Complexity:** `O(N)`, where `N` is the length of the string `s`. We iterate through the string once, performing a constant number of operations for each character.
- **Space Complexity:** `O(1)`. The DFA is represented by a small, fixed-size table, which is constant space.

---

## Implementation

See `solution.py` for the full implementation of both approaches.
