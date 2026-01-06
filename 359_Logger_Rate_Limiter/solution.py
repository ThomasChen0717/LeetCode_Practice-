# Approach 1: Queue and Set
from collections import deque

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_set = set()
        self._msg_queue = deque()
    
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        """
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
            else:
                break
        
        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp))
            return True
        else:
            return False

# Approach 2: HashMap
class Logger:

    def __init__(self):
        self.msg_last_print_t = {} 

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg_last_print_t: 
            self.msg_last_print_t[message] = timestamp 
            return True 
        
        last_print_time = self.msg_last_print_t[message]

        
        if timestamp - last_print_time < 10: return False 
        else: 
            self.msg_last_print_t[message] = timestamp
            return True
