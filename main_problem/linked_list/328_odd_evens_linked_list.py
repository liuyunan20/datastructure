# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_nodes = []
        even_nodes = []
        i = 1
        while head:
            if i % 2 == 0:
                even_nodes.append(head)
            else:
                odd_nodes.append(head)
            head = head.next
            i += 1
        dummy = ListNode()
        cur = dummy
        for node in odd_nodes:
            cur.next = node
            cur = cur.next
        for node in even_nodes:
            cur.next = node
            cur = cur.next
        cur.next = None
        return dummy.next
