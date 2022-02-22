# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # return a new liked list reverse to the input one
    def reverseList_1(self, head: ListNode) -> ListNode:
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

    # reverse the input linked list and return it
    def reverseList_2(self, head: ListNode) -> ListNode:
        l2 = None
        while head:
            l1 = ListNode(-1, head.next)
            head.next = l2
            l2 = head
            head = l1.next

        return l2
