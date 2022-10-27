# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_pos = set()
        while head and head not in node_pos:
            node_pos.add(head)
            head = head.next
        if head:
            return head
        return None
