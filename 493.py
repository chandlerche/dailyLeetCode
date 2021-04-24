class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        right_nums = []
        result = 0

        # 逆序遍历
        for i in nums[::-1]:
            
            # 使用二分查找，找到有多少个乘以2后的数字小于i
            result += bisect.bisect_left(right_nums, i)

            # 将当前的数字乘以2后，二分插入数组中
            bisect.insort(right_nums, 2 * i)

        return result