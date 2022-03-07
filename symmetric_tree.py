import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric_1(self, root: Optional[TreeNode]) -> bool:
        levelorder_tree = []
        my_stack = [[root]]
        while my_stack:
            current_level = collections.deque()
            next_level_nodes = []
            for node in my_stack.pop():
                if node:
                    current_level.append(node.val)
                    next_level_nodes.append(node.left)
                    next_level_nodes.append(node.right)
                else:
                    current_level.append("None")
            if next_level_nodes:
                my_stack.append(next_level_nodes)
            if current_level:
                levelorder_tree.append(current_level)
        for level in levelorder_tree[1:]:
            if len(level) % 2 == 1:
                return False
            else:
                while level:
                    if level.popleft() != level.pop():
                        return False
        return True

    def isSymmetric_2(self, root: Optional[TreeNode]) -> bool:
            levelorder_tree = []
            current_level_nodes = [root]
            while current_level_nodes:
                current_level = collections.deque()
                next_level_nodes = []
                for node in current_level_nodes:
                    if node:
                        current_level.append(node.val)
                        next_level_nodes.append(node.left)
                        next_level_nodes.append(node.right)
                    else:
                        current_level.append("None")
                current_level_nodes = next_level_nodes
                if current_level:
                    levelorder_tree.append(current_level)
            for level in levelorder_tree[1:]:
                if len(level) % 2 == 1:
                    return False
                else:
                    while level:
                        if level.popleft() != level.pop():
                            return False
            return True

    # solution using recursion
    def isSymmetric_recursion(self, root: Optional[TreeNode]) -> bool:
        return self.mirror(root, root)

    def mirror(self, node_left, node_right):
        if not node_left and not node_right:
            return True
        if not node_left or not node_right:
            return False
        if node_left.val == node_right.val and self.mirror(node_left.left, node_right.right) and self.mirror(node_left.right, node_right.left):
            return True
