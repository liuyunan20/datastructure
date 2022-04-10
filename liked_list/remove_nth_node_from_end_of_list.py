from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre_head = ListNode(0, head)
        node = head
        index = 1
        node_dict = {}
        while node:
            node_dict[index] = node
            node = node.next
            index += 1
        if node_dict.get(index - n + 1) and node_dict.get(index - n - 1):
            node_dict[index - n - 1].next = node_dict[index - n + 1]
            return head
        if node_dict.get(index - n - 1):
            node_dict[index - n - 1].next = None
            return head
        if node_dict.get(index - n + 1):
            return head.next
