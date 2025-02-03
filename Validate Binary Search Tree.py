# https://leetcode.com/problems/validate-binary-search-tree/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node):
            nonlocal prev_value

            if node is None:
                return True
            if not validate(node.left):
                return False
            if prev_value >= node.val:
                return False

            prev_value = node.val

            if not validate(node.right):
                return False
            return True

        prev_value = float('-inf')

        return validate(root)