from memory import Memory
import utilities, random

# This class simply adds a variable that will keep track of cache
# hits. This should be incremented in a subclass whenever the cache is
# hit.
class AbstractCache(Memory):
    def name(self):
        return "Cache"

    # Takes two parameters. Data is the data that forms the
    # "memory". Size is a non-negative integer that indicates the size
    # of the cache.
    def __init__(self, data, size=5):
        super().__init__(data)
        self.cache_hit_count = 0

    # Returns information on the number of cache hit counts
    def get_cache_hit_count(self):
        # TODO: Edit this code to correctly return the count of cache hits.
        return self.cache_hit_count
    
class CyclicCache(AbstractCache):
    def name(self):
        return "Cyclic"

    # TODO: Edit the code below to provide an implementation of a cache that
    # uses a cyclic caching strategy with the given cache size. You
    # can use additional methods and variables as you see fit as long
    # as you provide a suitable overridding of the lookup method.
    # Make sure that you increment cache_hit_count when appropriate!
    
    def __init__(self, data, size=5):
        super().__init__(data)
        self.size = size
        self.cache = {}
        self.data = data


    def lookup(self, key):
        if key in self.cache:
            self.cache_hit_count += 1
            return self.cache[key]
        else:
            value = super().lookup(key)
            self.insert(key, value)
            return value

    def insert(self, key, value):
        if len(self.cache) >= self.size:
            first_key = next(iter(self.cache))
            del self.cache[first_key]
        self.cache[key] = value

class LRUCache(AbstractCache):
    def name(self):
        return "LRU"

    # TODO: Edit the code below to provide an implementation of a cache that
    # uses a least recently used caching strategy with the given cache size.
    # You can use additional methods and variables as you see fit as
    # long as you provide a suitable overridding of the lookup method.
    # Make sure that you increment cache_hit_count when appropriate!
    
    def __init__(self, data, size=5):
        super().__init__(data)
        self.size = size
        self.cache = {}
        self.LRU = {}
        self.timestamp = 0
        self.data = data


    def lookup(self, key):
        if key in self.cache:
            self.LRU[key] = self.timestamp
            self.timestamp += 1
            self.cache_hit_count += 1
            return self.cache[key]
        else:
            value = super().lookup(key)
            self.insert(key, value)
            return value

    def insert(self, key, value):
        if len(self.cache) >= self.size:
            if self.cache:
                LRU_element = min(self.cache.keys(), key=lambda k: self.LRU[k])
                self.cache.pop(LRU_element)
                self.LRU.pop(LRU_element)
        self.cache[key] = value
        self.LRU[key] = self.timestamp
        self.timestamp += 1

class RandomCache(AbstractCache):
    def name(self):
        return "Random"

    # TODO: Edit the code below to provide an implementation of a cache that
    # uses a random eviction strategy with the given cache size.
    # You can use additional methods and variables as you see fit as
    # long as you provide a suitable overridding of the lookup method.
    # Make sure that you increment cache_hit_count when appropriate!
    
    def __init__(self, data, size=5):
        super().__init__(data)
        self.cache = {}
        self.size = size
        self.data = data


    def lookup(self, key):
        if key in self.cache:
            self.cache_hit_count += 1
            return self.cache[key]
        else:
            value = super().lookup(key)
            self.insert(key, value)
            return value

    def insert(self, key, value):
        if len(self.cache) >= self.size:
            random_key = random.choice(list(self.cache.keys()))
            del self.cache[random_key]
        self.cache[key] = value
