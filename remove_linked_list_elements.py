# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            new_head = head.next
            head = head.next

        new_head = head

        while head and head.next:
            while head.next and head.next.val == val:
                head.next = head.next.next
            head = head.next

        return new_head

    # use a pre_head as sentinel node
    def removeElements_2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pre_node = ListNode(-1, head)
        node = pre_node
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return pre_node.next
