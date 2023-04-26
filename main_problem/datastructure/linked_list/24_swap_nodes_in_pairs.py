# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        pre = ListNode()
        result = head.next
        while head and head.next:
            helper = head.next.next
            head.next.next = head
            pre.next = head.next
            head.next = helper
            pre = head
            head = helper
        return result
