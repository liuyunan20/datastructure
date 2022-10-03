class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = ListNode(-101, head)
        dummy = pre
        cur = head
        cur_dup = False
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur_dup = True
                cur.next = cur.next.next
            if cur_dup:
                pre.next = cur.next
                cur = cur.next
                cur_dup = False
            else:
                cur = cur.next
                pre = pre.next
        return dummy.next
