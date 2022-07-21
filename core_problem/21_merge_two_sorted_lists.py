# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from datastructure.linked_list_cycle import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = list1
        j = list2
        pre = cur = ListNode()
        while i and j:
            if i.val <= j.val:
                cur.next = i
                i = i.next

            else:
                cur.next = j
                j = j.next
            cur = cur.next
        if i:
            cur.next = i
        else:
            cur.next = j
        return pre.next
