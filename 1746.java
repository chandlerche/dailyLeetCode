public class Solution {
    
    private int res;
    
    /**
     * @param root: a Binary Search Tree (BST) with the root node
     * @return: the minimum difference
     */
    public int minDiffInBST(TreeNode root) {
        // Write your code here.
        res = Integer.MAX_VALUE;
        dfs(root);
        return res;
    }
    
    // 将cur子树的最小最大值包装成一个数组返回给上层递归
    private int[] dfs(TreeNode cur) {
        if (cur == null) {
            return null;
        }
        
        int[] left = null, right = null;
        int[] ret = {cur.val, cur.val};
        // 如果左子树不空，则用当前节点和左子树最大值的差来更新res，
        // 并将左子树最小值赋值给ret[0]
        if (cur.left != null) {
            left = dfs(cur.left);
            ret[0] = left[0];
            res = Math.min(res, cur.val - left[1]);
        }
        // 同上
        if (cur.right != null) {
            right = dfs(cur.right);
            ret[1] = right[1];
            res = Math.min(res, right[0] - cur.val);
        }
        
        return ret;
    }
}

class TreeNode {
    int val;
    TreeNode left, right;
    
    public TreeNode(int val) {
        this.val = val;
    }
}