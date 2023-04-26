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
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        i = 0
        n = len(nodes)
        while i + 1 < n:
            nodes[i], nodes[i + 1] = nodes[i + 1], nodes[i]
            i += 2
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]
