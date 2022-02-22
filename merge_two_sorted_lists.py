# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # solution I thought with many judgement
    def mergeTwoLists_1(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            if list1.val <= list2.val:
                head = list1
                l3 = list1
                list1 = list1.next

            else:
                head = list2
                l3 = list2
                list2 = list2.next

            while True:
                if list1 is None:
                    l3.next = list2
                    break
                elif list2 is None:
                    l3.next = list1
                    break
                elif list1.val <= list2.val:
                    l3.next = list1
                    l3 = l3.next
                    list1 = list1.next
                else:
                    l3.next = list2
                    l3 = l3.next
                    list2 = list2.next
            return head
    # solution of using a virtual previous node, then return .next of that node
    def mergeTwoLists_2(self, list1: ListNode, list2: ListNode) -> ListNode:
        new_head = ListNode()
        p_node = new_head
        while list1 and list2:
            if list1.val <= list2.val:
                p_node.next = list1
                list1 = list1.next
            else:
                p_node.next = list2
                list2 = list2.next
            p_node = p_node.next
        if list1 is None:
            p_node.next = list2
        else:
            p_node.next = list1
        return new_head.next
