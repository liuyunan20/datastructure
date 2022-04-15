# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        if not head:
            new_node.next = new_node
            return new_node
        if head == head.next:
            head.next = new_node
            new_node.next = head
            return head
        node = head
        node_set = set()
        max_node = head
        min_node = head
        while True:
            if node.val <= insertVal <= node.next.val:
                next_node = node.next
                node.next = new_node
                new_node.next = next_node
                return head
            node_set.add(node)
            if max_node.val <= node.val:
                max_node = node
            if min_node.val > node.val:
                min_node = node
            node = node.next
            if node in node_set:
                break
        if min_node.val < max_node.val:
            new_node.next = min_node
            max_node.next = new_node
        if min_node.val == max_node.val:
            next_node = node.next
            node.next = new_node
            new_node.next = next_node
        return head
