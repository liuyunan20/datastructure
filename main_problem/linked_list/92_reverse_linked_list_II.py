# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        nodes = []
        i = 1
        while i < left:
            pre = pre.next
            head = head.next
            i += 1
        left_hook = pre
        left_helper = head

        while i <= right:
            nodes.append(head)
            pre = pre.next
            head = head.next
            i += 1
        right_helper = pre
        right_hook = head

        dummy_hook = ListNode(0, right_helper)
        while nodes:
            node = nodes.pop()
            if nodes:
                node.next = nodes[-1]
            else:
                node.next = right_hook
        left_hook.next = dummy_hook.next
        return dummy.next
