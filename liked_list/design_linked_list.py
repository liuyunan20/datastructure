class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.root = None

    def get(self, index: int) -> int:
        node = self.root
        while node and index:
            node = node.next
            index -= 1
        if node:
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.root
        self.root = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        node = self.root
        if node:
            while node.next:
                node = node.next
            node.next = new_node
        else:
            self.root = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            new_node = ListNode(val)
            node = self.root
            while node and index - 1:
                node = node.next
                index -= 1
            if node:
                new_node.next = node.next
                node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.root:
            self.root = self.root.next
        else:
            node = self.root
            while index - 1:
                node = node.next
                index -= 1
            if node and node.next:
                node.next = node.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
