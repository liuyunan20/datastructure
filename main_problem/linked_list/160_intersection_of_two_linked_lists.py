# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list_a = []
        list_b = []
        while headA:
            list_a.append(headA)
            headA = headA.next
        while headB:
            list_b.append(headB)
            headB = headB.next
        m = len(list_a)
        n = len(list_b)
        offset = m - n
        if m >= n:
            list_a = list_a[offset:]
        if m < n:
            list_b = list_b[-offset:]
        while list_a and list_b:
            a = list_a.pop(0)
            b = list_b.pop(0)
            if a == b:
                return a
        return None

    def getIntersectionNode_smart(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while a != b:
            # traversal listA then listB head different part, arrive the intersection node
            a = a.next if a else headB
            # traversal listB then listA head different part, arrive the intersection node
            b = b.next if b else headA
        return a
