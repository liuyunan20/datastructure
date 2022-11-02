from sortedcontainers import SortedDict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nodes = SortedDict()
        while head:
            nodes.setdefault(head.val, [])
            nodes[head.val].append(head)
            head = head.next
        dummy = ListNode()
        node = dummy
        for key in nodes:
            for n in nodes[key]:
                node.next = n
                node = node.next

        node.next = None
        return dummy.next
