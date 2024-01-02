# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        def get_tree(node):
            if not node:
                return
            freq.setdefault(node.val, 0)
            freq[node.val] += 1
            get_tree(node.left)
            get_tree(node.right)
        get_tree(root)
        freq = sorted(freq.items(), key=lambda x: -x[1])
        result = [freq[0][0]]
        for i in range(1, len(freq)):
            if freq[i][1] < freq[i - 1][1]:
                return result
            result.append(freq[i][0])
        return result
