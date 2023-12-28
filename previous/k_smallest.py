class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        values = []
        arr = self.inorder(root,values)
        return arr[k-1]
    def inorder(self,root,a):
        if(root):
            self.inorder(root.left,a)
            a.append(root.val)  #Storing The Values in the Array which is passed as an argument
            self.inorder(root.right,a)
        return a