# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle_2(self, head: Optional[ListNode]) -> bool:
        # use hash table instead of list
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False

    def hasCycle_3(self, head: Optional[ListNode]) -> bool:
        faster = head
        while head and faster and faster.next:
            head = head.next
            faster = faster.next.next
            if head == faster:
                return True
        return False
