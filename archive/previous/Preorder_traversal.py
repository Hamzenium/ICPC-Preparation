"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def pr_order(root, output):
            if not root:
                return None
            output.append(root.val)
            for child in root.children:
                pr_order(child,output)
            return output
        return pr_order(root,[])
