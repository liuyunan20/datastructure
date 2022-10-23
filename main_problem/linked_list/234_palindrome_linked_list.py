# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        while len(nodes) >= 2:
            head = nodes.pop()
            tail = nodes.pop(0)
            if head != tail:
                return False
        return True
