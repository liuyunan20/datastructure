from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        index = 1
        odd = ListNode(0, head)
        even = ListNode(0, head.next)
        even_head = even
        node = head
        while node:
            if index % 2 == 1:
                odd.next = node
                odd = odd.next
            else:
                even.next = node
                even = even.next
            index += 1
            node = node.next
        odd.next = even_head.next
        even.next = None
        return head
