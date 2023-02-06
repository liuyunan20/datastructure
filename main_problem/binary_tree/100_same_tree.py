class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = [p]
        stack2 = [q]
        while stack1 or stack2:
            node1 = stack1.pop() if stack1 else None
            node2 = stack2.pop() if stack2 else None
            if (node1 and not node2) or (not node1 and node2):
                return False
            if not node1 and not node2:
                continue
            if not node1.left and not node1.right and not node2.left and not node2.right:
                if node1.val != node2.val:
                    return False
            else:
                stack1.append(node1.right)
                node1.right = None
                stack1.append(node1)
                stack1.append(node1.left)
                node1.left = None
                stack2.append(node2.right)
                node2.right = None
                stack2.append(node2)
                stack2.append(node2.left)
                node2.left = None

        return True
