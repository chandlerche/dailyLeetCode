from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # 方法1：时间On,空间O1
        if len(nums) == 0: return 0
        left = 0
        right = len(nums) - 1
        while True:
            pos = self.partition(nums , left , right)
            if pos + 1 == k:
                return nums[pos]
            elif pos + 1 > k:
                right = pos - 1
            else: # 说明是数组中第2大的数，但我们要的是第3大的，所以左指针移到当前pos的右边一位
                left = pos + 1

    def partition(self , nums , left , right):
        pivot = nums[left]
        l = left + 1     # 以left位的数为基准去比较大小，所以l指针要从left右一位开始
        r = right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums = self.swap(nums , l , r)
                l += 1
                r -= 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1
        nums = self.swap(nums , left , r) # 最后交换基准值和处在中间的r，使得交换后，基准值左边一定全比它大，右边全比它小
        return r

    def swap(self , nums , i , j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return nums

        '''
        # 方法2 优先队列 时间Onlogk 空间Ok
        if len(nums) == 0: return 0
        minHeap = PriorityQueue()
        for num in nums:
            minHeap.put(num)
            if minHeap.qsize() > k:
                minHeap.get()
        return minHeap.get()
        '''
