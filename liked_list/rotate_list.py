# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node = head
        node_dict = {}
        i = 0
        while node:
            i += 1
            node_dict[i] = node
            node = node.next
        k = k % i
        if not k:
            return head
        node_dict[i].next = node_dict[1]
        node_dict[i - k].next = None
        return node_dict[i - k + 1]
