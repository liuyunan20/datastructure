class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head, new):
            if not head:
                return new
            hook = head.next
            head.next = new
            return helper(hook, head)
        return helper(head, None)
