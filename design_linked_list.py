class MyLinkedList:

    def __init__(self):
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        node = self.next
        if index > 0:
            for _ in range(index - 1):
                node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        new_node = MyLinkedList()
        new_node.val = self.val
        new_node.next = self.next
        self.val = val
        self.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = MyLinkedList()
        new_node.val = val
        if not self.next:
            self.next = new_node
        else:
            node = self.next
            while node.next:
                node = node.next
            node.next = new_node
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            new_node = MyLinkedList()
            new_node.val = val
            if index == 1:
                new_node.next = self.next
                self.next = new_node
            else:
                while index - 1:
                    node = node.next
                    index -= 1
                new_node.next = node.next
                node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.next:
                self.val = self.next.val
                self.next = self.next.next
            else:
                self.val = None
        else:
            node = self.next
            if index == 1:
                self.next = node.next
            else:
                while index - 2:
                    node = node.next
                if node.next:
                    node.next = node.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
