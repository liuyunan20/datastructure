# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 0:
            return head
        i = 1
        nodes = {}
        while head:
            nodes[i] = head
            head = head.next
            i += 1

        k = k % (i - 1)
        if i == 2 or k == 0:
            return nodes[1]
        nodes[i - 1 - k].next = None
        nodes[i - 1].next = nodes[1]
        return nodes[i - k]
