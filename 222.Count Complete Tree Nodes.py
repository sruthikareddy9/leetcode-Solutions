# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        def height(node):
            h=0
            while node:
                h+=1
                node=node.left
            return h
        lh=height(root.left)
        rh=height(root.right)
        if lh==rh:
            return (2**lh)+self.countNodes(root.right)
        else:
            return self.countNodes(root.left)+(2**rh)
        
