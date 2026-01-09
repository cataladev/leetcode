# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return [True, 0]

            hR = dfs(curr.right)
            hL = dfs(curr.left)

            balance = hR[0] and hL[0] and abs(hL[1] - hR[1]) <= 1
            return [balance, 1 + max(hL[1], hR[1])]
        return dfs(root)[0]