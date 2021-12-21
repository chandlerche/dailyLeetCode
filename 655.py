# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getHeight(root):
            if not root:
                return 0
            return 1+max(getHeight(root.left),getHeight(root.right))
        heigh=getHeight(root)
        width=2**heigh-1
        self.res=[["" for i in range(width)] for _ in range(heigh)]
        def fill(root,i,l,r):
            if not root:
                return
            mid=l+(r-l)//2
            self.res[i][mid]=""+str(root.val)
            fill(root.left,i+1,l,mid-1)
            fill(root.right,i+1,mid+1,r)
        fill(root,0,0,width)
        return self.res