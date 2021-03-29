class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        nums.append(0)
        stack=[-1]
        ans=0
        for i in range(len(nums)):

            while nums[i]< nums[stack[-1]]:
                h=nums[stack.pop()]
                w=i-1-stack[-1]
                if i-1>=k and stack[-1]+1<=k:
                    ans=max(ans,h*w)
            
            stack.append(i)

        
        nums.pop()
        return ans