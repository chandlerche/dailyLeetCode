public class Solution {
    
    int max = 0;
    public int largestBSTSubtree(TreeNode root) {
        _largestBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
        return max;
    }
    
    // use null value as sign of broken BST condition
    private Integer _largestBST(TreeNode node, int minVal, int maxVal){
        if (node == null) return 0;
        
        Integer left = _largestBST(node.left, minVal, node.val);
        Integer right = _largestBST(node.right, node.val, maxVal);
        
        // independent research of subtrees has sense only if they aren't BST 
		// with current limitations on min and max
        if (left == null) _largestBST(node.left, Integer.MIN_VALUE, Integer.MAX_VALUE);
        if (right == null) _largestBST(node.right, Integer.MIN_VALUE, Integer.MAX_VALUE);
        
        if (left == null || right == null) return null;
        
        if (minVal < node.val && node.val < maxVal) {
            max = Math.max(max, 1 + left + right);
            return 1 + left + right;
        }
        return null;
    }
}