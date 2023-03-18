"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        copied = {None: None}
        while node:
            copied[node] = Node(node.val)
            node = node.next
        node = copied[head]
        result = node
        while node:
            node.next = copied[head.next]
            node.random = copied[head.random]
            node = node.next
            head = head.next
        return result
