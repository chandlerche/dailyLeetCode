class Solution:    
    def permuteUnique(self, nums: list) -> list:
        
        hash_num = dict()
        
        for item in nums:
            hash_num[item] = hash_num.get(item,0) + 1
        output = []
        
        def backtrack(combination:list):
            
            if len(combination) == len(nums):
                output.append(combination)
            else:
                for num_key in list(hash_num.keys()):
                    
                    hash_num[num_key] = hash_num.get(num_key,0) - 1

                    if hash_num.get(num_key,0) == 0: 
                        hash_num.pop(num_key)

                    backtrack(combination + [num_key])
                    hash_num[num_key] = hash_num.get(num_key,0) + 1
        
        backtrack([])
        
        return output