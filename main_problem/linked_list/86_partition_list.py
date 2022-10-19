# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        find_big = False
        pre = ListNode(0, head)
        result = pre
        while head:
            if find_big == False and head.val >= x:
                find_big = True
                hook_p = pre
                hook_b = head
                head = head.next
                pre = pre.next
            elif find_big == True and head.val < x:
                current = head.next
                pre.next = current
                hook_p.next = head
                head.next = hook_b
                hook_p = head
                head = current
            else:
                pre = pre.next
                head = head.next
        return result.next
