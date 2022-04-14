"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs_child(node):
            while node and (node.next or node.child):
                if node.child:
                    next_node = node.next
                    node.next = node.child
                    node.child.prev = node
                    node.child = None
                    node = dfs_child(node.next)
                    node.next = next_node
                    if next_node:
                        next_node.prev = node
                if node.next:
                    node = node.next
            return node
                       
        if not head:
            return head
        node = head
        dfs_child(node)
        return head
