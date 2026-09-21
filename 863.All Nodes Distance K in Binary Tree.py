# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent={}
        def dfs(node,par):
            if node:
                parent[node]=par
                dfs(node.left,node)
                dfs(node.right,node)
        dfs(root,None)
        queue=[target]
        visited={target}
        distance=0
        result=[]
        while queue:
            if distance==k:
                return[node.val for node in queue]
            for i in range(len(queue)):
                node=queue.pop(0)
                for neighbour in[node.left,node.right,parent[node]]:
                    if neighbour and neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            distance+=1
        return result

        
