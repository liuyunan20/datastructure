# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            l1 = ListNode(head.val, None)
            l2 = l1
            while head.next:
                l2 = ListNode(head.next.val, l1)
                l1 = l2
                head = head.next
        else:
            l2 = None
        return l2
