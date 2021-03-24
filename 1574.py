class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        import bisect
        # 右侧最长升序子序列
        right_begin = 0
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                right_begin = i
                break

        # 删除左侧所有数字的长度
        result = right_begin
        if result == 0:
            return 0

        # 左侧最长上升子序列
        for i in range(0, len(arr)):
            if i > 0 and arr[i] < arr[i - 1]:
                break
            # 二分查找当前数字在右侧可插入的位置，当前数字的下标和插入位置之间的数字可被删除
            index = bisect.bisect_left(arr, arr[i], right_begin)
            result = min(result, index - 1 - i)
            # print(arr[i], index, result)
        return result