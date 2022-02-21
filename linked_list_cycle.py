# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle_1(self, head: ListNode) -> bool:
            exist = []
            if not head or not head.next:
                return False
            current = head.next
            while True:
                if not current.next:
                    return False
                if current in exist:
                    return True
                exist.append(current)
                current = current.next

    def hasCycle_2(self, head: ListNode) -> bool:
        exist = []
        while head:
            if head in exist:
                return True
            exist.append(head)
            head = head.next
        return False

