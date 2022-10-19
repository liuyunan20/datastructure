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
            return head
        visited = {None: None}
        new_head = Node(head.val)
        visited[head] = new_head

        while head:
            if head not in visited:
                new_node = Node(head.val)
                visited[head] = new_node
            else:
                new_node = visited[head]
            if head.next and head.next not in visited:
                new_node.next = Node(head.next.val)
                visited[head.next] = new_node.next
            else:
                new_node.next = visited[head.next]
            if head.random and head.random not in visited:
                new_node.random = Node(head.random.val)
                visited[head.random] = new_node.random
            else:
                new_node.random = visited[head.random]
            head = head.next
        return new_head
