# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = dummy
        duplicate = False
        while node:
            if node.next and node.next.next and node.next.val == node.next.next.val:
                node.next = node.next.next
                duplicate = True
            elif duplicate:
                node.next = node.next.next
                duplicate = False
            else:
                node = node.next
        return dummy.next
