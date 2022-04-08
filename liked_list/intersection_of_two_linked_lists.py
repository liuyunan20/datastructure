# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode_tle(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while a:
            while b:
                if a == b:
                    return a
                b = b.next
            a = a.next
            b = headB
        return None
    # solution using list of all node value
    def getIntersectionNode_2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        a_list = []
        b_list = []
        while a:
            a_list.append(a.val)
            a = a.next
        while b:
            b_list.append(b.val)
            b = b.next
        a_list = a_list[::-1]
        b_list = b_list[::-1]
        i = 0
        for a, b in zip(a_list, b_list):
            if a != b:
                break
            i += 1
        if i == 0:
            return None
        a_index = len(a_list) - i
        b_index = len(b_list) - i
        a, b = headA, headB
        while a_index:
            a = a.next
            a_index -= 1
        while b_index:
            b = b.next
            b_index -= 1
        while a != b:
            a = a.next
            b = b.next
        return a
