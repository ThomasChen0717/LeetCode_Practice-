# 359. Logger Rate Limiter

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Hash Table, Queue, Set

---

## Problem Description

Design a logger system that receives a stream of messages along with their timestamps. Each **unique** message should only be printed **at most every 10 seconds** (i.e. a message printed at timestamp `t` will prevent other identical messages from being printed until timestamp `t + 10`).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the `Logger` class:

- `Logger()` Initializes the `logger` object.
- `bool shouldPrintMessage(int timestamp, string message)` Returns `true` if the `message` should be printed in the given `timestamp`, otherwise returns `false`.
 

---

## Examples
Example: 
```
Input
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output
[null, true, true, false, false, false, true]

Explanation
Logger logger = new Logger();
logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
```

## Constraints

- `0 <= timestamp <= 10^9`
- Every `timestamp` will be passed in non-decreasing order (chronological order).
- `1 <= message.length <= 30`
- At most `10^4` calls will be made to `shouldPrintMessage`.

---

## Approach 1: Queue + Set
### Intuition

We use a queue to store the messages and a set to store the unique messages.
When a message arrives, we check the timestamp for any messages in the queue that are older than 10 seconds. 
We remove the expired messages. 
Then we check if the message is in the set.
If the message is not in the set, we add it to the set and return `true`.
Otherwise, we return `false`.

### Complexity Analysis
`N` is the size of the queue.
- **Time Complexity:** `O(1)`
While in the worst case a single call might remove up to N obsolete messages from the queue (where N is the number of messages in the queue), each message is added and removed at most once. So over multiple calls, the total work is linear, and the average (amortized) cost per call remains constant.
- **Space Complexity:** `O(N)`
---

## Approach 2: HashMap

### Intuition

We use a hash map to store the messages and their timestamps.
When a message arrives, we check if the message is in the hash map.
If the message is not in the hash map, we add it to the hash map and return `true`.
Otherwise, we check if the timestamp is greater than or equal to the timestamp in the hash map plus 10.
If it is, we update the timestamp in the hash map and return `true`.
Otherwise, we return `false`.

### Complexity Analysis
`M` is the number of unique messages.
- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(M)`

## Implementation

See `solution.py` for the full implementation.
