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
        if not head:
            return None
        result = Node(0)
        node = result
        mapping = {}
        pre = head
        while head:
            node.val = head.val
            node.next = None if head.next == None else Node(0)
            mapping[head] = node
            head = head.next
            node = node.next
        node = result
        while pre:
            print(pre.val)
            node.random = mapping[pre.random] if pre.random else None
            if pre.random:
                print(pre.random.val)
            pre = pre.next
            if pre:
                print(pre.val)
            node = node.next
        return result
