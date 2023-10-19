# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            leftdepth = self.maxDepth(root.left)
            rightdepth = self.maxDepth(root.right)
        return 1 + max(leftdepth, rightdepth)

def array_to_tree(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    root.left = array_to_tree(nums[:mid])
    root.right = array_to_tree(nums[mid + 1:])

    return root


algorithm = Solution()
array = [1, 2, 3, 4, 5, 6, 7]
root_node = array_to_tree(array)
inverted_tree = algorithm.maxDepth(root_node)
print(inverted_tree)
""" we have devised the depth first search algorithm for the problem through recursion and 
based on the master theorem is O(n), if the root is none we return 0
else, we recursively call root.left and root.right, and use max to get atleast 1 or 0, then we finally we add 1 to final return """