from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = []
        val2 = []
        while l1:
            val1.append(l1.val)
            l1 = l1.next
        while l2:
            val2.append(l2.val)
            l2 = l2.next
        nodes = []
        helper = 0
        while val1 or val2:
            l1 = val1.pop() if val1 else 0
            l2 = val2.pop() if val2 else 0
            nodes.append((l1 + l2 + helper) % 10)
            helper = (l1 + l2 + helper) // 10
        if helper:
            nodes.append(helper)
        print(nodes)
        head = ListNode(nodes[-1], None)
        node = head
        for i in range(len(nodes) - 2, -1, -1):
            node.next = ListNode(nodes[i], None)
            node = node.next
        return head
