# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def copy_node(node):
            if not node:
                return None
            new_node = Node(node.val)
            new_node.next = copy_node(node.next)
            node_dict[node] = new_node
            return new_node
        node_dict = {}
        new_head = copy_node(head)
        node = head
        while node:
            if node.random:
                node_dict[node].random = node_dict[node.random]
            node = node.next
        return new_head
