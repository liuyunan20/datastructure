# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        result = 0
        while nodes:
            result = max(result, nodes.pop(0) + nodes.pop())
        return result
