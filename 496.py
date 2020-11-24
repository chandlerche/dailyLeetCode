class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        array = []
        mark = 0
        for i in nums1:
            index2 = nums2.index(i)
            for j in range(index2, len(nums2)):
                if nums2[j] > i:
                    array.append(nums2[j])
                    mark = 1
                    break
            if mark:
                mark = 0
                continue
            array.append(-1)
        return array