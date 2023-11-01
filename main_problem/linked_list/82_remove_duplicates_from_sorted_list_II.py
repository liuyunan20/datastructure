class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        result = ListNode(0)
        result.next = head
        pre = result
        duplicate = False
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
                duplicate = True
            if duplicate:
                pre.next = head.next if head.next else None
                duplicate = False
            else:
                pre = pre.next
            head = head.next
        return result.next
