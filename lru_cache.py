class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val 
        self.next = None 
        self.prev = None 
class linked_list:
    def __init__(self,capacity):
        self.capacity = capacity 
        self.left_node = Node(0,0)
        self.right_node = Node(0,0)
        self.hashmap = {}
        self.left_node.next = self.right_node
        self.right_node.prev = self.left_node
    def put(self, key,val):
        if key in self.hashmap:
            new_node = self.hashmap[key]
            prev = new_node.prev
            nxt = new_node.next
            prev.next = nxt 
            nxt.prev = prev
        new_node = Node(key,val)
        self.hashmap[key] = new_node
        prev = self.right_node.prev
        nxt = self.right_node 
        prev.next = new_node
        new_node.next = nxt 
        nxt.prev = new_node 
        new_node.prev = prev
        if len(self.hashmap) > self.capacity:
            lru = self.left_node.next
            prev = lru.prev
            nxt = lru.next
            prev.next = nxt 
            nxt.prev = prev
            del self.hashmap[lru.key]
        curr = self.left_node 
    def get(self,key):
        if key in self.hashmap:
            new_node = self.hashmap[key]
            prev = new_node.prev
            nxt = new_node.next
            prev.next = nxt 
            nxt.prev = prev 
            prv = self.right_node.prev 
            nxt = self.right_node 
            prv.next = new_node 
            new_node.prev = prv
            prv.next = nxt 
            nxt.prev = new_node 
            return self.hashmap[key].val
        return -1
ll = linked_list(2)
for i in range(3):
    method = input("enter method: ")
    if method == "put":
        print(ll.put(int(input("enter key: ")),int(input("enter value: "))))
    else:
        print(ll.get(int(input("enter key: "))))