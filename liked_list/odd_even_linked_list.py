# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node_dict = {}
        i = 1
        while head:
            node_dict[i] = head
            head = head.next
            i += 1
        x = 1
        while node_dict.get(x + 2):
            node_dict[x].next = node_dict[x + 2]
            x += 2
        y = 2
        if node_dict.get(y):
            node_dict[x].next = node_dict[y]
            while node_dict.get(y + 2):
                node_dict[y].next = node_dict[y + 2]
                y += 2
            node_dict[y].next = None
        return node_dict[1]
