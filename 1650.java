public class Solution {
    public Node lowestCommonAncestor(Node p, Node q) {
        int lenp = 0, lenq = 0;
        Node pp = p, qq = q;
        while (pp != null) {
            lenp++;
            pp = pp.parent;
        }
        while (qq != null) {
            lenq++;
            qq = qq.parent;
        }
        
        if (lenp < lenq) {
            Node tmp = p;
            p = q;
            q = tmp;
        }
        
        for (int i = 0; i < Math.abs(lenp - lenq); i++) {
            p = p.parent;
        }
        
        while (p != q) {
            p = p.parent;
            q = q.parent;
        }
        
        return p;
    }
}

class Node {
    int val;
    Node left, right, parent;
    
    public Node(int val) {
        this.val = val;
    }
}