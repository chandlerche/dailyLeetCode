import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode[] nodes) {
        Set<TreeNode> set = new HashSet<>(Arrays.asList(nodes));
        return dfs(root, set);
    }
    
    private TreeNode dfs(TreeNode root, Set<TreeNode> set) {
        if (root == null) {
            return null;
        }
        
        if (set.contains(root)) {
            return root;
        }
    
        TreeNode left = dfs(root.left, set), right = dfs(root.right, set);
        if (left != null && right != null) {
            return root;
        }
        
        return left == null ? right : left;
    }
}

class TreeNode {
    int val;
    TreeNode left, right;
    
    public TreeNode(int val) {
        this.val = val;
    }
}