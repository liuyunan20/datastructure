from typing import Optional

from datastructure.linked_list_cycle import ListNode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.cycle_length = 1

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if self.hasCycle(head):
            i = head
            j = head
            while True:
                for _ in range(self.cycle_length):
                    j = j.next
                if i == j:
                    return i
                i = i.next
                j = i


    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        i = head
        j = head.next
        while i and j and j.next:
            i = i.next
            j = j.next.next
            if i == j:
                j = j.next
                while i != j:
                    j = j.next
                    self.cycle_length += 1
                return True
        return False
