from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        position = 1
        to_reverse = []
        dummy = ListNode(-1, head)
        left_tail = dummy
        reverse = False
        while head and position != right:
            if position == left:
                node = head
                tail = head
                reverse = True
            if not reverse:
                left_tail = left_tail.next
                head = head.next
            else:
                right_head = head.next
                head.next = node
                node = head
                head = right_head

            position += 1

        if reverse:
            right_head = head.next
            head.next = node
            left_tail.next = head
            tail.next = right_head
        return dummy.next



