from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def get_inorder(node):
            tree = []
            if not node:
                return tree
            tree += get_inorder(node.left)
            tree.append(node.val)
            tree += get_inorder(node.right)
            return tree
        inorder_tree = get_inorder(root)
        diff = abs(target - inorder_tree[0])
        n = len(inorder_tree)
        closest_idx = n - 1
        for i in range(n):
            if diff < abs(target - inorder_tree[i]):
                closest_idx = i - 1
                break
            diff = abs(target - inorder_tree[i])
        i = 1
        j = -1
        result = [inorder_tree[closest_idx]]
        while k - 1:
            if 0 <= closest_idx + j < closest_idx + i < n:
                if abs(target - inorder_tree[closest_idx + i]) < abs(target - inorder_tree[closest_idx + j]):
                    result.append(inorder_tree[closest_idx + i])
                    i += 1
                else:
                    result.append(inorder_tree[closest_idx + j])
                    j -= 1
            elif 0 <= closest_idx + j:
                result.append(inorder_tree[closest_idx + j])
                j -= 1
            elif closest_idx + i < n:
                result.append(inorder_tree[closest_idx + i])
                i += 1
            k -= 1
        return result

    def closestKValues_iterator(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        stack = [root]
        inorder_tree = []
        closest_idx = -1
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                if len(inorder_tree) == 1 and inorder_tree[0] >= target:
                    closest_idx = 0
                if inorder_tree and inorder_tree[-1] <= target <= node.val:
                    if target - inorder_tree[-1] < node.val - target:
                        closest_idx = len(inorder_tree) - 1
                    else:
                        closest_idx = len(inorder_tree)
                inorder_tree.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)
                    node.right = None
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                    node.left = None
        n = len(inorder_tree)
        if closest_idx == -1:
            closest_idx = n - 1
        i = 1
        j = -1
        result = [inorder_tree[closest_idx]]
        while k - 1:
            if 0 <= closest_idx + j < closest_idx + i < n:
                if abs(target - inorder_tree[closest_idx + i]) < abs(target - inorder_tree[closest_idx + j]):
                    result.append(inorder_tree[closest_idx + i])
                    i += 1
                else:
                    result.append(inorder_tree[closest_idx + j])
                    j -= 1
            elif 0 <= closest_idx + j:
                result.append(inorder_tree[closest_idx + j])
                j -= 1
            elif closest_idx + i < n:
                result.append(inorder_tree[closest_idx + i])
                i += 1
            k -= 1
        return result
