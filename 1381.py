class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.queue = []
        self.maxSize = maxSize


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.queue) < self.maxSize:
            self.queue.append(x)
        


    def pop(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue.pop()
        else:
            return -1


    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(min(k, len(self.queue))):
            self.queue[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)