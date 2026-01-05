from collections import deque
class b_tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class binary_tree:
    def __init__(self,):
        self.queue = deque()
    def insert_node_data(self,root,data):
        if not root:
            return b_tree(data)
        elif root.data > data:
                root.left = self.insert_node_data(root.left,data)
        else:
            root.right = self.insert_node_data(root.right,data)
        return root
    def implement_b_tree(self,root,data):
        if not root:
            return b_tree(data)
        elif not root.left:
            root.left = self.implement_b_tree(root.left,data)
        elif not root.right:
            root.right = self.implement_b_tree(root.right,data)
        else:
            root.left = self.implement_b_tree(root.left,data)
        return root
    def display(self,root):
        if not root:
            return 
        self.display(root.left)
        print(root.data,end="->")
        self.display(root.right)
    def same_tree(self,p,q):
        if not p and not q:
            return True
        if not p or not q or (p.data != q.data):
            return False
        return self.same_tree(p.left,q.left) and self.same_tree(p.right,q.right)
    def dfs(self,root):
        if not root:
            return 0
        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)
        return 1+max(left_height,right_height)
    def invert_tree(self,root):
        if not root:
            return None
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        root.left,root.right =  root.right, root.left
        return root
        
    def level_order(self,root):
        if root is not None:
            self.queue.append(root)
            while self.queue:
                temp=self.queue.popleft()
                print(temp.data,end="->")
                if temp.left is not None:
                    self.queue.append(temp.left)
                if temp.right is not None:
                    self.queue.append(temp.right) 
obj = binary_tree()
root = None
# p=None
# q=None
# nodes_p = [1,2,3]
# nodes_q = [1,1]
tree_nodes = [1,2,2,3,4,4,3]
for i in tree_nodes:
    root = obj.insert_node_data(root,i)
    # p = obj.implement_b_tree(p,i)
    # q = obj.implement_b_tree(q,i)
print(obj.display(root))
# print(obj.invert_tree(root))
print(obj.display(root))
print(obj.level_order(root))
# print(obj.display(q))
# print(obj.same_tree(p,q))
# print(obj.dfs(root))
