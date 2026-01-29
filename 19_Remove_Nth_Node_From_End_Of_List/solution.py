# Approach 1: Two Pass 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head 
        length = 0 
        first = head
        while first is not None:
            length += 1 
            first = first.next 

        steps = length - n

        second = head 

        for _ in range(steps): 
            second = second.next

        second.next = second.next.next

        return dummy.next

# Approach 2: One Pass
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head 
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next 
        
        while first is not None: 
            first = first.next 
            second = second.next
        
        second.next = second.next.next

        return dummy.next