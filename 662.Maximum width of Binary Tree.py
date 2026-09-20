# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        queue=[(root,0)]
        max_width=0
        while queue:
            levelsize=len(queue)
            firstindex=queue[0][1]
            for i in range(levelsize):
                node,index=queue.pop(0)
                index=index-firstindex
                if i==0:
                    left=index
                if i==levelsize-1:
                    right=index
                if node.left:
                    queue.append((node.left,2*index+1))
                if node.right:
                    queue.append((node.right,2*index+2))
            width=right-left+1
            max_width=max(max_width,width)
        return max_width

        
