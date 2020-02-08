print "Hello World"


# key = lambda n:self.lru[n]
# print(key())

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        # print(self.capacity)
        self.track = 0
        self.lru = {}
        self.cache = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.lru[key] = self.track
            self.track += 1
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.cache) >= self.capacity:
            a_key = min(self.lru.keys(), key=lambda n: self.lru[n])
            # print(a_key)
            self.cache.pop(a_key)
            self.lru.pop(a_key)
        self.cache[key] = value
        self.lru[key] = self.track
        self.track += 1


# LRUCache cache = new LRUCache( 2 /* capacity */ );
if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # returns 1
    cache.put(3, 3)  # remove key 2
    # cache.get(2);  # returns -1 (not found)
    print(cache.get(2))
    cache.put(4, 4)    # remove key 1
    print(cache.get(1))       # returns -1 (not found)
    print cache.get(3)       # returns 3
    print cache.get(4)       # returns 4

# a={1:1, 2:2}
# print(a)
# a.pop(1)
# print(a)
