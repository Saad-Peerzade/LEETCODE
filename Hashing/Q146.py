class Node(object):
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}         

    
        self.head = Node()            
        self.tail = Node()            
        self.head.next = self.tail
        self.tail.prev = self.head


    def _add_to_front(self, node):
        """Place node right after head (mark as most recent)."""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        """Detach node from the list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_front(self, node):
        """Node was accessed/updated: move it to the most-recent position."""
        self._remove(node)
        self._add_to_front(node)

    def _pop_lru(self):
        """Remove and return the least-recently-used node (before tail)."""
        lru = self.tail.prev
        self._remove(lru)
        return lru


    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_to_front(node)   
        return node.val

    def put(self, key, value):
        if key in self.map:
           
            node = self.map[key]
            node.val = value
            self._move_to_front(node)
            return

       
        node = Node(key, value)
        self.map[key] = node
        self._add_to_front(node)

        
        if len(self.map) > self.cap:
            lru = self._pop_lru()
            del self.map[lru.key]
