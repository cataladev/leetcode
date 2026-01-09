class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7

        # Postorder list (nodes in root-left-right, then reversed => left-right-root)
        stack = [root]
        post = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            post.append(node)
            stack.append(node.left)
            stack.append(node.right)

        # 1) total sum
        total = 0
        for node in post:
            total += node.val

        # 2) subtree sums + best product (process in postorder)
        sub = {}  # node -> subtree sum
        best = 0
        for node in reversed(post):  # left-right-root
            s = node.val
            if node.left:
                s += sub[node.left]
            if node.right:
                s += sub[node.right]
            sub[node] = s
            best = max(best, s * (total - s))

        return best % MOD
