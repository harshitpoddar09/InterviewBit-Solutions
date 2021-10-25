from collections import OrderedDict
class LRUCache:
 
    # @param capacity, an integer
    def __init__(self, capacity):
        self.d=OrderedDict()
        self.capacity=capacity        
 
    # @return an integer
    def get(self, key):
        if key not in self.d:
            return -1
        val=self.d.pop(key)
        self.d[key]=val
        return val        
 
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.d:
            self.d.pop(key)
        self.d[key]=value
        if len(self.d)>self.capacity:
            self.d.popitem(last=False)  