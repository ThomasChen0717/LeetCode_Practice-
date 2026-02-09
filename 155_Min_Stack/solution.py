# Approach 1: Stack with pair (num, min)
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: 
            self.stack.append((val, val))
            return
        
        current_min = self.stack[-1][1]
        self.stack.append((val, min(val, current_min)))


    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Approach 2: Two Stacks
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val) 

        if not self.min_stack or val <= self.min_stack[-1]: 
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]: 
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
# Approach 3: Optimized approach 2
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val) 

        if self.min_stack and val == self.min_stack[-1][0]: 
            self.min_stack[-1][1] += 1 
        elif not self.min_stack or val < self.min_stack[-1][0]: 
            self.min_stack.append([val, 1]) 

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1][0]: 
            self.min_stack[-1][1] -= 1
        
        if self.min_stack[-1][1] == 0: 
            self.min_stack.pop()
            
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]
        