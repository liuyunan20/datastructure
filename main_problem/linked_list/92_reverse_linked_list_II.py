# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        result = head
        nodes = []
        while head:
            if i == left - 1:
                hook_left = head
            if left <= i <= right:
                nodes.append(head)
            i += 1
            head = head.next
        hook_right = nodes[-1].next
        start = nodes.pop()
        current = start
        while nodes:
            current.next = nodes.pop()
            current = current.next
        current.next = hook_right
        if left == 1:
            return start
        else:
            hook_left.next = start
            return result
