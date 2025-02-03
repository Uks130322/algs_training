# https://leetcode.com/problems/symmetric-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        if root.left and not root.right or not root.left and root.right:
            return False
        left_branch = [root.left.val]
        right_branch = [root.right.val]

        def dfs(root, go_left=True):
            nonlocal left_branch
            nonlocal right_branch
            if go_left:
                if not root.left and not root.right:
                    left_branch += ['null', 'null']
                elif root.left:
                    left_branch.append(root.left.val)
                    dfs(root.left)
                if root.right:
                    if not root.left:
                        left_branch.append('null')
                    left_branch.append(root.right.val)
                    dfs(root.right)

            else:
                if not root.left and not root.right:
                    right_branch += ['null', 'null']
                elif root.right:
                    right_branch.append(root.right.val)
                    dfs(root.right, go_left=False)
                if root.left:
                    if not root.right:
                        right_branch.append('null')
                    right_branch.append(root.left.val)
                    dfs(root.left, go_left=False)

        dfs(root.left)
        dfs(root.right, go_left=False)
        return left_branch == right_branch
