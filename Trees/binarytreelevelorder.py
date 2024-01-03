class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder_better(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return 
        def dfs(node, depth):
            if not node:
                return
            if depth >= len(result):
                result.append([])
            result[depth].append([node.val])
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        depth = 0
        dfs(root, depth)
        return result
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = None  # Represents null
root.right.left = None  # Represents null
root.right.right = TreeNode(5)

solution = Solution()
print(solution.levelOrder_better(root))


def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    result = []
    if not root:
        return 
    result.append([root.val])
    def traversal(root):
        level = []
        if not root:
            return 
        if root.left :
            level.append(root.left.val)
        if root.right:
            level.append(root.right.val)
        if len(level) >= 1:
            result.append(level)
        traversal(root.left)
        traversal(root.right)
    traversal(root)
    return result