from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self,):
        self.index = -1
        self.queue = deque()
    def implement_tree(self,root,i):
        if root is None:
            return Node(i)
        #new_node = Node(nodes[self.index])
        elif root.data > i:
            root.left = self.implement_tree(root.left,i)
        elif root.data < i:
            root.right = self.implement_tree(root.right,i)
        return root
    def display(self,root):
        if root is None:
            return 
        print(root.data,end="->")
        self.display(root.left)
        self.display(root.right)
    def post_order(self,root):
        if root is None:
            return 
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data,end="->")
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
    def dfs(self,root):
        if root is None:
            return 0
        left_depth = self.dfs(root.left)
        right_depth = self.dfs(root.right)
        return 1+max(left_depth,right_depth)
    def inorder(self,root):
        if root is None:
            return 
        self.inorder(root.left)
        print(root.data,end=",")
        self.inorder(root.right)  
bt = BinaryTree()
#nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
root = None
nodes = [10,5,15,13,2,7,1,6,18,20]
for i in nodes:
    root = bt.implement_tree(root,i)
print(root.data)
print(bt.display(root))
print(bt.post_order(root))
print(bt.level_order(root))
print(bt.dfs(root))
print(bt.inorder(root))