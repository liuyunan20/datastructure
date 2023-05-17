# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        twin = {}
        i = 0
        while head:
            twin[i] = head.val
            i += 1
            head = head.next
        result = 0
        for x in range(i // 2):
            result = max(result, twin[x] + twin[i-1-x])
        return result
