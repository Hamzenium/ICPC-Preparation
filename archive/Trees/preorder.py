class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    if root is None:
        return []
    
    result = []
    
    # Visit the current node
    result.append(root.val)
    
    # Recursively visit the left subtree
    result.extend(preorderTraversal(root.left))
    
    # Recursively visit the right subtree
    result.extend(preorderTraversal(root.right))
    
    return result

def postorderTraversal(root):
    if root is None:
        return []
    
    result = []
    
    # Recursively visit the left subtree
    result.extend(postorderTraversal(root.left))
    
    # Recursively visit the right subtree
    result.extend(postorderTraversal(root.right))
    
    # Visit the current node
    result.append(root.val)
    
    return result


def inorderTraversal(root):
    if root is None:
        return []
    
    result = []
    
    # Recursively visit the left subtree
    result.extend(inorderTraversal(root.left))
    
    # Visit the current node
    result.append(root.val)
    
    # Recursively visit the right subtree
    result.extend(inorderTraversal(root.right))
    
    return result