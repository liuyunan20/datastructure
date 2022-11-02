# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_nodes = []
        l2_nodes = []
        while l1:
            l1_nodes.append(l1.val)
            l1 = l1.next
        while l2:
            l2_nodes.append(l2.val)
            l2 = l2.next
        carrier = 0
        nodes = []
        while l1_nodes or l2_nodes or carrier:
            val1 = l1_nodes.pop() if l1_nodes else 0
            val2 = l2_nodes.pop() if l2_nodes else 0
            value = val1 + val2 + carrier
            nodes.append(value % 10)
            carrier = value // 10
        dummy = ListNode()
        cur = dummy
        print(nodes)
        while nodes:
            cur.next = ListNode(nodes.pop())
            cur = cur.next
        return dummy.next

    def addTwoNumbers_2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_nodes = []
        l2_nodes = []
        while l1:
            l1_nodes.append(l1.val)
            l1 = l1.next
        while l2:
            l2_nodes.append(l2.val)
            l2 = l2.next
        carrier = 0
        cur = ListNode(0, None)

        while l1_nodes or l2_nodes or carrier:
            val1 = l1_nodes.pop() if l1_nodes else 0
            val2 = l2_nodes.pop() if l2_nodes else 0
            value = val1 + val2 + carrier
            cur.val = value % 10
            dummy = ListNode(0, cur)
            cur = dummy
            carrier = value // 10

        return dummy.next
