# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_val = []
        while head:
            node_val.append(head.val)
            head = head.next
        if node_val == node_val[::-1]:
            return True
        return False
