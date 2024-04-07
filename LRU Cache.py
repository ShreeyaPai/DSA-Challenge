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

###################### LINKED LIST IMPLEMENTATION

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
