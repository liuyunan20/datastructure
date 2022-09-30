# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        i = list1
        j = list2
        pre = cur = ListNode()
        while i and j:
            if i.val <= j.val:
                cur.next = i
                i = i.next

            else:
                cur.next = j
                j = j.next
            cur = cur.next
        if i:
            cur.next = i
        else:
            cur.next = j
        return pre.next

    def mergeTwoLists_2(self, list1: ListNode, list2: ListNode) -> ListNode:
        result = ListNode()
        node = result
        while list1 and list2:
            if list1.val < list2.val:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next
            node = node.next

        node.next = list1 if list1 else list2
        return result.next
