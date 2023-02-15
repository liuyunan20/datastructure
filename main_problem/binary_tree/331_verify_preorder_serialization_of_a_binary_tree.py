class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == "#":
            return True
        preorder = preorder.split(',')
        print(preorder)
        val = preorder.pop(0)
        if val == "#":
            return False
        root = TreeNode(int(val))
        stack = [root]
        left = True
        while preorder:
            val = preorder.pop(0)
            if val != "#":
                node = TreeNode(int(val))
                if not stack:
                    return False
                parent = stack.pop()
                if left:
                    if parent.left:
                        return False
                    parent.left = node
                    stack.append(parent)
                else:
                    if parent.right:
                        return False
                    parent.right = node
                stack.append(node)
                left = True
            if val == "#":
                if not stack:
                    return False
                if left:
                    node = stack.pop()
                    if node.left:
                        return False
                    node.left = None
                    left = False
                    stack.append(node)
                else:
                    node = stack.pop()
                    if node.right:
                        return False
                    node.right = None
        if stack:
            return False
        return True
