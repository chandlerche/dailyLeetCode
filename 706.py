lass MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_list = []
        self.val_list = []
        self.key_set = set()
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key in self.key_set:
            index = self.key_list.index(key)
            self.val_list[index] = value
        else:
            self.key_list.append(key)
            self.key_set.add(key)
            self.val_list.append(value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key not in self.key_set:
            return -1
        else:
            index = self.key_list.index(key)
            return self.val_list[index]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.key_set:
            self.key_set.remove(key)
            index = self.key_list.index(key)
            del self.key_list[index]
            del self.val_list[index]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)