class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
       # 搜索不到返回-1
        if key not in self.cache:
            return -1
        # 取出缓存中的key并赋值
        self.cache[key] = self.cache.pop(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # 如存在就先删除key
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
       # 取缓存列表中最先进入的key
        if len(self.cache) > self.capacity:
            x = list(self.cache)[0]
            self.cache.pop(x)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)