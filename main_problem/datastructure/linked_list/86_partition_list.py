# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        dummy_l = ListNode()
        left = dummy_l
        dummy_r = ListNode()
        right = dummy_r
        for node in nodes:
            if node.val >= x:
                right.next = node
                right = right.next
            if node.val < x:
                left.next = node
                left = left.next
        right.next = None
        left.next = dummy_r.next
        return dummy_l.next
