class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        # day天是否可以制作m束花
        def count(day):
            sums = 0
            nums = 0
            for i in range(n):
                if nums >= m:
                    break
                if bloomDay[i] <= day:
                    sums += 1
                else:
                    sums = 0
                if sums == k:
                    nums += 1
                    sums = 0
            return nums >= m
        
        Days = sorted(set(bloomDay))
        l = 0;r = len(Days)-1
        while l <= r:
            mid = (l+r)>>1
            if count(Days[mid]):
                r = mid - 1
            else:
                l = mid + 1
        return Days[l]