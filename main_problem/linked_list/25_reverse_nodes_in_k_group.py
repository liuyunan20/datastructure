class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        i = 0
        group = []
        dummy = ListNode(0)
        left = dummy
        while head:
            group.append(head)
            head = head.next
            i += 1
            if i == k:
                while group:
                    left.next = group.pop()
                    print(left.val)
                    left = left.next
                i = 0

        left.next = group[0] if group else None

        return dummy.next
