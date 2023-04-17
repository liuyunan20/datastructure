# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes_tle(self, head: Optional[ListNode]) -> List[int]:
        i = 0
        answer = []
        nodes = {}
        while head:
            answer.append(0)
            nodes[i] = head
            discard = []
            for j in nodes:
                if head.val > nodes[j].val:
                    answer[j] = head.val
                    discard.append(j)
            for j in discard:
                nodes.pop(j)
            i += 1
            head = head.next
        return answer
