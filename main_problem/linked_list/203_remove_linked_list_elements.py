# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        while head:
            if head.val == val:
                pre.next = head.next
                head = head.next
            else:
                head = head.next
                pre = pre.next
        return dummy.next
