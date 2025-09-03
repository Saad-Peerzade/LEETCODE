class Solution(object):
    def __init__ (self):
        self.bucket_counts=1009
        self.buckets=[[] for _ in range (self.bucket_counts)]
    
    def __bucket_index (self,key):
        return key % self.bucket_counts
    
    def add(self,key):
        idx=self._bucket_index(key)
        buckets=self.buckets[idx]
        
        if key not in buckets:
            buckets.append(key)

    def remove (self,key):
        idc = self._bucket_index(key)
        buckets=self.buckets[idx]
        try:
            buckets.remove(key)
        except ValueError:
            pass

    def contains(self,key):
        idx=self.buckets_index(key)
        buckets=self.buckets[idx]
        return key in buckets