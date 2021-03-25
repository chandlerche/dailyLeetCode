class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1,nums2=Counter(nums1),Counter(nums2)
        res=0
        for nums1,nums2 in (nums1,nums2),(nums2,nums1):
            for i,x in nums1.items():
                for j,y in nums1.items():
                    if sqrt(i*j) in nums2:
                        if i!=j:
                            res+=x*y*nums2[sqrt(i*j)]
                        else:
                            res+=x*(x-1)*nums2[sqrt(i*j)]
        return res//2