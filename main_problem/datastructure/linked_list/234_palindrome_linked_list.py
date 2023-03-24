class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        i = 0
        j = len(vals) - 1
        while i <= j:
            if vals[i] != vals[j]:
                return False
            i += 1
            j -= 1
        return True
