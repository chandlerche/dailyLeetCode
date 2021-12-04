/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    //使用前序遍历的方式，但是需要给空节点添加 N 的占位符
    public String serialize(TreeNode root) {
        // 表示空节点
        if (root == null) {
            return "N,";
        }
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(root.val);
        // 因为有负数或则多位数的存在会占多个字符，所以考虑用分隔符
        stringBuilder.append(",");
        stringBuilder.append(serialize(root.left));
        stringBuilder.append(serialize(root.right));

        return stringBuilder.toString();

    }


    public TreeNode deserialize(String data) {
        if ("".equals(data) || data == null || "N,".equals(data)) {
            return null;
        }
        // 去掉最后一个多余的 ，
        String substring = data.substring(0, data.length() - 1);
        // 分割成数组
        String[] result = substring.split(",");
        // 先将第一个头节点保存
        TreeNode treeNode = new TreeNode(Integer.parseInt(result[0]));
        getNextNode(result, 0, treeNode);
        return treeNode;
    }
    // item 序列化树的数组
    // start 当前节点在数组中的位置
    // node 当前节点
    private int getNextNode(String[] item, int start, TreeNode node) {
        if (start >= item.length) {
            return start;
        }
        // 如果两个子节点为空 直接跳过
        if ("N".equals(item[start + 1]) && "N".equals(item[start + 2])) {
            return start + 3;
        }
        // 头节点已被保存了，所以跳过该节点
        int nextNodeIndex = start + 1;
        // 左节点不为空 就连接上
        if (!"N".equals(item[nextNodeIndex])) {
            TreeNode leftNode = new TreeNode(Integer.parseInt(item[nextNodeIndex]));
            node.left = leftNode;
            nextNodeIndex = getNextNode(item, nextNodeIndex, leftNode);
        } else {
            // 空跳过
            nextNodeIndex++;
        }
        // 右节点不为空 就连接上
        if (!"N".equals(item[nextNodeIndex])) {
            TreeNode rightNode = new TreeNode(Integer.parseInt(item[nextNodeIndex]));
            node.right = rightNode;
            nextNodeIndex = getNextNode(item, nextNodeIndex, rightNode);
        }else{
            nextNodeIndex++;
        }
        // 返回下一个节点的位置
        return nextNodeIndex;
    }
}