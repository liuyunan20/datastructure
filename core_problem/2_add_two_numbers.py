class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Optional:
    pass


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        pre = result
        carry = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            val = (a + b + carry) % 10
            carry = (a + b + carry) // 10
            node = ListNode(val, None)
            pre.next = node
            pre = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            node.next = ListNode(1, None)
        return result.next
