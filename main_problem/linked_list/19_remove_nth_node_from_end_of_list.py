# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        nodes = {}
        result = head
        while head:
            nodes[i] = head
            i += 1
            head = head.next
        if i - n > 0:
            nodes[i - n - 1].next = nodes[i - n + 1] if n != 1 else None
            return result
        else:
            return result.next
