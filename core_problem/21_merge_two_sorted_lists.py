# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        result = ListNode()
        node = result
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                node = list1
                list1 = list1.next
            else:
                node.next = list2
                node = list2
                list2 = list2.next
        if list1:
            node.next = list1
        else:
            node.next = list2
        return result.next
