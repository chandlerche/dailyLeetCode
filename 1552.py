class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        right = (position[-1] - position[0]) // (m - 1)
        left = 1
        
        def check(interval):
            cnt = 1
            
            i = 0
            j = 1
            while j < len(position):
                if position[j] - position[i] >= interval:
                    cnt += 1
                    if cnt >= m:
                        return True
                    i = j
                j += 1
                
            return False
        
        while left < right:
            mid = left + (right - left + 1) // 2
            if not check(mid):
                right = mid - 1
            else:
                left = mid
        
        return left