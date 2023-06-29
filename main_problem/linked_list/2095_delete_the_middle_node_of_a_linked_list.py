# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        mid = len(nodes) // 2
        if mid == 0:
            return None
        nodes[mid - 1].next = nodes[mid + 1] if mid + 1 < len(nodes) else None
        return nodes[0]
