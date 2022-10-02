class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        result = ListNode(0, head)
        hook = result
        while head:
            reverse_nodes = []
            cur_head = head
            for i in range(k):
                if not head:
                    hook.next = cur_head
                    return result.next
                reverse_nodes.append(head)
                head = head.next
            head_k = reverse_nodes.pop()
            cur = head_k
            while reverse_nodes:
                cur.next = reverse_nodes.pop()
                cur = cur.next
            hook.next = head_k
            hook = cur
            cur.next = None
        return result.next
