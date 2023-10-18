# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

def array_to_tree(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    root.left = array_to_tree(nums[:mid])
    root.right = array_to_tree(nums[mid + 1:])

    return root

# Create an instance of the Solution class
algorithm = Solution()

array = [1, 2, 3, 4, 5, 6, 7]
root_node = array_to_tree(array)
inverted_tree = algorithm.invertTree(root_node)


def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val, end=' ')
        in_order_traversal(root.right)

# Call the in-order traversal on the inverted_tree
in_order_traversal(inverted_tree)


# You can now work with the inverted_tree as needed.


""" The algorithm that we have developed has the time complexity of O(n), so we have the root of the array, when we have the root of the array
we then use left child of the root and replae the pointer of the root with the right one , and then recursive call the fuinction to go thoough the
array be defining a newer root until there in none left  """