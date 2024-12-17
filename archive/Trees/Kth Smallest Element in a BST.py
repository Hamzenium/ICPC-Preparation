# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        result = []
        def traversal(root):
            if not root:
                return 
            traversal(root.left)
            result.append(root.val)
            traversal(root.right)
            return
        traversal(root)
        result[k-1]

solution = Solution()
root = [5,3,6,2,4,null,null,1]
print(solution.kthSmallest(root,3))