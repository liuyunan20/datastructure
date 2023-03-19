# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        val_node = {}
        while head:
            val_node.setdefault(head.val, []).append(head)
            head = head.next
        val = list(val_node.keys())
        val.sort()
        dummy = ListNode()
        node = dummy
        for i in range(len(val)):
            for j in range(len(val_node[val[i]])):
                node.next = val_node[val[i]][j]
                node = node.next
        node.next = None
        return dummy.next
