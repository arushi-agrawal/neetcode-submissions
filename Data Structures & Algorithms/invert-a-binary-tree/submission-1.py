# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def dfs(self, node):
    #     if not node:
    #         return
    #     self.dfs(node.left)
    #     self.dfs(node.right)

    #     node.left,node.right=node.right,node.left
    #     # node.left = self.dfs(node.right)
    #     # node.right = self.dfs(node.left)

    #     return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue=deque([root])

        while queue:
            curr=queue.popleft()
            if not curr:
                continue
            curr.left, curr.right = curr.right, curr.left
            queue.append(curr.left)
            queue.append(curr.right)

        
        return root










