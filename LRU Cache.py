class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache={}
        self.capacity=capacity
        self.q=collections.deque()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.q:
            self.q.remove(key)
            self.q.append(key)
        return self.cache.get(key, -1)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        alr=self.cache.get(key, -1)
        if len(self.cache)==self.capacity and alr==-1:
            least=self.q.popleft()
            del self.cache[least]
        self.cache[key]=value
        if key in self.q:
            self.q.remove(key)
        self.q.append(key)
        # print(self.cache)
        # print(self.q)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
