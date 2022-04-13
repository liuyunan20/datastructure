from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        node = result
        helper = 0
        while l1 or l2:
            if l1 and l2:
                val = (l1.val + l2.val + helper) % 10
                node.val = val
                helper = (l1.val + l2.val + helper) // 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = (l1.val + 0 + helper) % 10
                node.val = val
                helper = (l1.val + 0 + helper) // 10
                l1 = l1.next
            elif l2:
                val = (0 + l2.val + helper) % 10
                node.val = val
                helper = (0 + l2.val + helper) // 10
                l2 = l2.next
            if l1 or l2:
                node.next = ListNode()
                node = node.next
        if helper == 1:
            node.next = ListNode(1)
        return result
