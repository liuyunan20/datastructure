# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        nodes = {}
        while True:
            complete = True
            for i in range(len(lists)):
                if lists[i]:
                    complete = False
                    nodes.setdefault(lists[i].val, []).append(lists[i])
                    lists[i] = lists[i].next
            if complete:
                break
        nodes = sorted(nodes.items())
        dummy = ListNode()
        result = dummy
        while nodes:
            x = nodes.pop(0)
            while x[1]:
                node = x[1].pop()
                dummy.next = node
                dummy = dummy.next
        dummy.next = None
        return result.next
