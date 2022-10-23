# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        dummy = ListNode()
        pre = dummy
        while nodes:
            pre.next = nodes.pop()
            pre = pre.next
        pre.next = None
        return dummy.next
