class Solution:
    def isBalanced(self, root):
        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return height(root) != -1
