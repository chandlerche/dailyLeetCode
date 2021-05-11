class Solution:
    def quickSort(self, nums, left, right):
        if left < right:
            low, high = left, right
            cuValue = nums[low]
            while low < high:
                while low < high and cuValue + nums[high] >= nums[high] + cuValue:
                    high -= 1
                if low < high:
                    nums[low] = nums[high]
                while low < high and cuValue + nums[low] <= nums[low] + cuValue:
                    low += 1
                if low < high:
                    nums[high] = nums[low]
            nums[low] = cuValue
            self.quickSort(nums, left, low - 1)
            self.quickSort(nums, low + 1, right)

    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(num) for num in nums]
        self.quickSort(nums_str, 0, len(nums_str) - 1)
        ans = ''.join(nums_str)
        return '0' if not int(ans) else ans