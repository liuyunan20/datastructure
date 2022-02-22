# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = ListNode(-1, head)
        p_node = new_head

        while head and head.next:
            if head.val == head.next.val:
                p_node.next = head.next
            else:
                p_node = head
            head = head.next
        return new_head.next
