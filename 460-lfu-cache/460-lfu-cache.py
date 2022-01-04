class LFUCache:

    
    # this problem gets solved by making both get and put in O(1)
    # that is done by having a dict for key, value and another dict with a double linkedlist for frequency count
    # the second linked list also attached most frequently used item to top of the list, thus tail gives the LRU
    # this problem is very interesting as it required some thinking and causing me to adopt a DLL approach which I usually don't
    
    class Node :
        def __init__(self, key, val, l=None,r=None, freq=0) :
            self.key = key
            self.val = val
            self.l = l
            self.r = r
            self.freq = freq
    
    
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.c = {}
    
    
    def removeNode(self, node) :
        left = node.l
        right = node.r
        if left :
            left.r = right
        if right :
            right.l = left
        head,tail = self.c[node.freq]
        if head == node :
            if right :
                head = right
            else :
                del self.c[node.freq]
                return
        if tail == node :
            tail = left     #should never be null
        self.c[node.freq] = (head,tail)

    def addNode(self, node) :
        node.l = None
        node.r = None
        if node.freq in self.c :
            head,tail = self.c[node.freq]
            node.r = head
            head.l = node
            head = node
        else :
            head = node
            tail = node
            
        self.c[node.freq] = (head,tail)
    
    def get(self, key: int) -> int:
        if self.capacity == 0 : return -1
        if key in self.d :
            node = self.d[key]
            self.removeNode(node)
            node.freq += 1
            self.addNode(node)
            
            return node.val
        else :
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0 : return
        if key in self.d :
            node = self.d[key]
            self.removeNode(node)
            node.val = value
            node.freq += 1
            self.addNode(node)
        else :
            if len(self.d.keys()) == self.capacity :
                minfreq = min(self.c.keys())
                # picking tail also filters out least recently used node
                _,tailnode = self.c[minfreq]
                self.removeNode(tailnode)
                del self.d[tailnode.key]
                
            node = LFUCache.Node(key, value)
            node.freq = 1
            self.d[key] = node
            self.addNode(node)