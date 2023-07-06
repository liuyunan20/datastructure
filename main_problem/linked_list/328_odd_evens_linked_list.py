# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 1
        odd = ListNode()
        dummy = odd
        hook = ListNode()
        even = hook
        while head:
                       even.next = head
                even = head
            else:
                odd.next = head
                odd = head
            head = head.next
            i += 1
        odd.next = hook.next
        even.next = None
        return dummy.next
