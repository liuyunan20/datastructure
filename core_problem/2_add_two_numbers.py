class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Optional:
    pass


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0)
        result = node
        helper = 0
        while l1 and l2:
            node.val = (l1.val + l2.val + helper) % 10
            helper = (l1.val + l2.val + helper) // 10
            node.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
            pre_node = node
            node = node.next

        while l1:
            node.val = (l1.val + helper) % 10
            helper = (l1.val + helper) // 10
            node.next = ListNode(0)
            l1 = l1.next
            pre_node = node
            node = node.next

        while l2:
            node.val = (l2.val + helper) % 10
            helper = (l2.val + helper) // 10
            node.next = ListNode(0)
            l2 = l2.next
            pre_node = node
            node = node.next

        if helper == 1:
            node.val = 1
        else:
            pre_node.next = None

        return result

    def addTwoNumbers_2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        result = node
        helper = 0;
        while l1 or l2 or helper:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + helper
            node.next = ListNode(val % 10)
            helper = val // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            node = node.next

        return result.next
