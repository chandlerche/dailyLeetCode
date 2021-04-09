# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        stk = [root]
        ans = list()
        idx = 0
        while stk:
            top = stk.pop()
            while top:
                if top.val != voyage[idx]:
                    return [-1]
                idx += 1
                if top.left and top.right and top.right.val == voyage[idx]:
                    stk.append(top.left)
                    top = top.right
                    ans.append(voyage[idx - 1])
                else:
                    if top.right:
                        stk.append(top.right)
                    top = top.left
        return ans