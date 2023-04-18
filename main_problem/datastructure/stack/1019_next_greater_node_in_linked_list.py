# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        answer = []
        i = 0
        while head:
            answer.append(0)
            while stack and stack[-1][0] < head.val:
                answer[stack[-1][1]]= head.val
                stack.pop()
            stack.append((head.val, i))
            i += 1
            head = head.next
        return answer
