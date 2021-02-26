class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        root = TreeNode(-1)
        
        for num in nums:
            cur_node = root 
            
            for i in range(0, 32):          
                # print num, 1 <<(31 - i), num & (1 <<(31 - i))
                if num & (1 <<(31 - i)) == 0:    
                    if not cur_node.left:
                        cur_node.left = TreeNode(0)
                    cur_node = cur_node.left
                else:                         
                    if not cur_node.right:
                        cur_node.right = TreeNode(1)
                    cur_node = cur_node.right
            cur_node.left = TreeNode(num)      
                    
        res = 0
        for num in nums:
            cur_node = root
            
            for i in range(0, 32):
                # print cur_node.val, cur_node.left, cur_node.right
                if num & (1 <<(31 - i)) == 0:     
                    if cur_node.right:           
                        cur_node = cur_node.right
                    else:                        
                        cur_node = cur_node.left
                else:                            
                    if cur_node.left:            
                        cur_node = cur_node.left
                    else:                        
                        cur_node = cur_node.right
            temp = cur_node.left.val             
                
            res = max(res, num ^ temp)           
                
        return res