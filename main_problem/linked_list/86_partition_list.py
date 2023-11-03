# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        left = []
        right = []
        while head:
            if head.val < x:
                left.append(head)
            else:
                right.append(head)
            head = head.next
        result = ListNode(0)
        cur = result
        left.extend(right)
        for node in left:
            cur.next = node
            cur = node
        cur.next = None
        return result.nextt
        return result.next
