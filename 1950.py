def findMaximums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        
        def append_to_deque(q, index):
            while q and nums[q[-1]] > nums[index]:
                q.pop()
            q.append(index)
        
        # for windows from 1 to n
        for window_size in range(1, n+1):
            start = 0 
            max_val = float('-inf')
            q = deque()
            for end in range(n):
                # monotonic stack keep track of min element in window
                append_to_deque(q, end)
                if  end-start+1 >= window_size:
                    max_val = max(max_val, nums[q[0]])
                    
                    # if element to be removed is on stack remove
                    if start == q[0]:
                        q.popleft()
                    start+=1
            res.append(max_val)            
        return res