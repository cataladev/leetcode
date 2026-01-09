class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q: return root
        minr = min(p.val, q.val)
        maxr = max(p.val, q.val)
        while root:
            if minr > root.val:
                root = root.right
            elif maxr < root.val:
                root = root.left
            else:
                return root