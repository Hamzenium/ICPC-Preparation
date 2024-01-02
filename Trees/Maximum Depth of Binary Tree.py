# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = left = self.maxDepth(root.right)

        return 1 + max(left, right)


solution = Solution()
root = [3,9,20,null,null,15,7]
print(solution.maxDepth(root))