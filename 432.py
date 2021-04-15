class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_map = {}
        self.value_map = {}
        self.max_value = None
        self.min_value = None

    def value_map_add(self, key, cnt):
        if cnt == 0:
            return
        cnt_set = self.value_map.get(cnt)
        if cnt_set is None:
            cnt_set = set()
            self.value_map[cnt] = cnt_set
        set.add(cnt_set, key)

        if self.max_value is None or cnt > self.max_value:
            self.max_value = cnt
        if self.min_value is None or cnt < self.min_value:
            self.min_value = cnt

    def value_map_del(self, key, cnt):
        if cnt == 0:
            return
        cnt_set = self.value_map.get(cnt)
        if cnt_set is not None:
            set.remove(cnt_set, key)
            if not cnt_set:
                del self.value_map[cnt]
        if not self.value_map:
            self.max_value = None
            self.min_value = None

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        old_value = self.key_map.get(key, 0)
        new_value = old_value + 1
        self.key_map[key] = new_value
        self.value_map_add(key, new_value)
        self.value_map_del(key, old_value)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        old_value = self.key_map.get(key, 0)
        if old_value == 0:
            return
        new_value = old_value - 1
        self.key_map[key] = new_value
        self.value_map_add(key, new_value)
        self.value_map_del(key, old_value)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.max_value is None:
            return ''
        else:
            while self.max_value not in self.value_map:
                self.max_value -= 1
            for x in self.value_map[self.max_value]:
                return x

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.min_value is None:
            return ''
        else:
            while self.min_value not in self.value_map:
                self.min_value += 1
            for x in self.value_map[self.min_value]:
                return x



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()